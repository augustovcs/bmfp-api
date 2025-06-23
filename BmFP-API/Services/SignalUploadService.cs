using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using BmFP_API.DTOs;

namespace BmFP_API.Services
{
    public class SignalUploadService
    {
        private readonly HttpClient _httpClient;

        public SignalUploadService(HttpClient httpClient)
        {
            _httpClient = httpClient;
        }

        public async Task<string> UploadSignalAsync(SignalUploadDTO dto)
        {

            using var content = new MultipartFormDataContent();

            if (dto.FileDAT != null)
            {
                var fileContentDAT = new StreamContent(dto.FileDAT.OpenReadStream());
                fileContentDAT.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue(dto.FileDAT.ContentType);
                content.Add(fileContentDAT, "FileDAT", dto.FileDAT.FileName);
            }

            if (dto.FileHEA != null)
            {
                var fileContentHEA = new StreamContent(dto.FileHEA.OpenReadStream());
                fileContentHEA.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue(dto.FileHEA.ContentType);
                content.Add(fileContentHEA, "FileHEA", dto.FileHEA.FileName);
            }

            var response = await _httpClient.PostAsync("http://localhost:5000/api/access", content);

            string responseContent = await response.Content.ReadAsStringAsync();

            if (!response.IsSuccessStatusCode)
            {
                Console.WriteLine($"Erro {response.StatusCode}: {responseContent}");
                throw new Exception($"Erro sending signal: {response.StatusCode} - {responseContent}");
            }

            else
            {
                Console.WriteLine($"Signal uploaded successfully: {responseContent}");
                return responseContent;
            }
        
        }
    }
}
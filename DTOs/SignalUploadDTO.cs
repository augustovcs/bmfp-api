namespace BmFP_API.DTOs;

public class SignalUploadDTO
{
    public IFormFile File { get; set; }
    public string SignalType { get; set; }
    public double SampleRate { get; set; }
    
}
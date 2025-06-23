using BmFP_API.DTOs;
using Microsoft.AspNetCore.Mvc;
using BmFP_API.Services;
using Microsoft.AspNetCore.Http.Timeouts;
namespace BmFP_API.Controllers;


[ApiController]
[Route("api/signal/[controller]")]
public class SignalController : ControllerBase
{

    [HttpPost]
    [RequestTimeout(30000000)] 
    public async Task<IActionResult> UploadSignal([FromForm] SignalUploadDTO dto, [FromServices] SignalUploadService service)
    {
        var result = await service.UploadSignalAsync(dto);
        return Ok(result);
    }

    
    
}
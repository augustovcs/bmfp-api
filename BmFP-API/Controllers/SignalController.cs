using BmFP_API.DTOs;
using Microsoft.AspNetCore.Mvc;

namespace BmFP_API.Controllers;


[ApiController]
[Route("api/signal/[controller]")]
public class SignalController : ControllerBase
{
    
    [HttpPost]
    public ActionResult<string> UploadSignal([FromForm] SignalUploadDTO dto)
    {
        
        return "ok";
        
    }
    
}
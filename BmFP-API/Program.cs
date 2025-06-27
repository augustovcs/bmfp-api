using BmFP_API.Services;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddHttpClient<SignalUploadService>(client =>
{
    client.Timeout = TimeSpan.FromMinutes(15); // Set a timeout of 5 minutes
    client.BaseAddress = new Uri("http://localhost:5000/api/access");
});

builder.Services.AddCors();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

builder.Services.AddControllers();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI(c =>
    {
        c.ConfigObject.AdditionalItems["requestTimeout"] = "30000000"; // Set the request timeout to 5 minutes in Swagger UI
    });
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
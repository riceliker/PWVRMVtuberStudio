using Godot;
using Godot.Collections;
using System;
using System.IO;
namespace PWVrmVtuberStudio;

public class HttpInit
{
    public HttpInit()
    {
        HttpClient http_client = new HttpClient();
        http_client.ConnectToHost("127.0.0.1", GetConfigJson.getPort());
    }
}

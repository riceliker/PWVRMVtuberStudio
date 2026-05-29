using Godot;
using Godot.Collections;
using System;
using System.IO;
namespace PWVrmVtuberStudio;

public static class GetConfigJson
{
    /// <summary>
    /// Get config.json root data.
    /// </summary>
    /// <returns></returns>
    /// <exception cref="Exception"></exception>
    private static Dictionary getConfigJsonFile()
    {
        string godotProjectDir = ProjectSettings.GlobalizePath("res://");
        string pythonDir = Path.Combine(godotProjectDir, "..");
        string jsonPath = Path.Combine(pythonDir, "config.json");

        using var file = Godot.FileAccess.Open(jsonPath, Godot.FileAccess.ModeFlags.Read);
        if (file == null)
        {
            throw new Exception("ERROR: Config Json not found");
        }
        string json_content = file.GetAsText();
        file.Close();
        return Json.ParseString(json_content).AsGodotDictionary();
    }
    public static int getPort()
    {
        Dictionary root = getConfigJsonFile();
        Dictionary http = root["http"].AsGodotDictionary();
        return http["port"].AsInt32();
    }
}
using Godot;
using System;
namespace PWVrmVtuberStudio;
public partial class Preload : Node
{
    public override void _Ready()
    {
        new HttpInit();
    }
}

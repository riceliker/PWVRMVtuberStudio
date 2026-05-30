extends Node

func get_api_url(path: String) -> String:
	var engine_dict = JavaScriptBridge.eval("""
    (function() {
        return {
            host: window.location.host,       
            protocol: window.location.protocol
        }
    })()
	""", true)
	
	var protocol = engine_dict.protocol
	var host = engine_dict.host
	return protocol + "//" + host + path

func call_api(path: String, on_result: Callable):
	var url = get_api_url(path)
	
	var req = HTTPRequest.new()
	add_child(req)
	
	req.request_completed.connect(func(_result, _code, _headers, body):
		var data = body.get_string_from_utf8()
		on_result.call(data)
		req.queue_free()
	)
	
	req.request(url)

func _ready() -> void:
	call_api("/test", func(data):
		print(data)

	)

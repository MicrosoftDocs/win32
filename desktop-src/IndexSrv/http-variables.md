---
Description: HTTP Variables
ms.assetid: fdda75f9-a7bc-40f4-9087-f12a29bb12f0
title: HTTP Variables
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HTTP Variables

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Several variables in HTML extension files can give a lot of information about the environment and Web client connected to the server. In addition, all headers sent by the client are available. For Indexing Service to access these headers, you must convert them:

1.  Add HTTP\_ to the beginning.
2.  Convert all hyphens to underscores.
3.  Convert all letters to uppercase.

The following list gives a listing of default variables.

<dl> <dt>

<span id="ALL_HTTP"></span><span id="all_http"></span>ALL\_HTTP
</dt> <dd>

All HTTP headers that were not already parsed into one of the listed variables. These variables are of the form HTTP\_header field name with successive variables separated by a new line character, for example:

HTTP\_ACCEPT: \*/\*, q=0.300, audio/x-aiff, audio/basic, image/jpeg, image/gif, text/plain, text/html

HTTP\_USER\_AGENT: Microsoft Internet Explorer/0.1 (Win32)

HTTP\_REFERER: http://webserver/samples/dbsamp/dbsamp3.htm

HTTP\_CONTENT\_TYPE: application/x-www-form-urlenPRE: 10

HTTP\_EXTENSION: Security/Digest

</dd> <dt>

<span id="AUTH_TYPE"></span><span id="auth_type"></span>AUTH\_TYPE
</dt> <dd>

The type of authorization in use. If the user name has been authenticated by the server, this will contain Basic. NTLM returns the value **Negotiate**. Otherwise, it will not be present.

</dd> <dt>

<span id="CONTENT_LENGTH"></span><span id="content_length"></span>CONTENT\_LENGTH
</dt> <dd>

The number of bytes that the script can expect to receive from the client.

</dd> <dt>

<span id="CONTENT_TYPE"></span><span id="content_type"></span>CONTENT\_TYPE
</dt> <dd>

The content type of the information supplied in the body of a request by a POST variable.

</dd> <dt>

<span id="GATEWAY_INTERFACE"></span><span id="gateway_interface"></span>GATEWAY\_INTERFACE
</dt> <dd>

The revision of the CGI specification with which this server complies. The current version is Common Gateway Interface 1.1.

</dd> <dt>

<span id="HTTP_ACCEPT"></span><span id="http_accept"></span>HTTP\_ACCEPT
</dt> <dd>

Special-case HTTP header. Values of the Accept: fields are concatenated, separated by ", "; for example, if the following lines are part of the HTTP header: accept: \*/\*; q=0.1 accept: text/html accept: image/jpeg then the HTTP\_ACCEPT variable will have a value of: \*/\*; q=0.1, text/html, image/jpeg.

</dd> <dt>

<span id="PATH_INFO"></span><span id="path_info"></span>PATH\_INFO
</dt> <dd>

Additional path information, as given by the client. This comprises the trailing part of the URL after the script name but before the query string (if any).

</dd> <dt>

<span id="PATH_TRANSLATED"></span><span id="path_translated"></span>PATH\_TRANSLATED
</dt> <dd>

This is the value of PATH\_INFO, but with any virtual path name expanded into a directory specification.

</dd> <dt>

<span id="QUERY_STRING"></span><span id="query_string"></span>QUERY\_STRING
</dt> <dd>

The information that follows the question mark (?) in the URL that referenced this script.

</dd> <dt>

<span id="REMOTE_ADDR"></span><span id="remote_addr"></span>REMOTE\_ADDR
</dt> <dd>

The IP address of the client.

</dd> <dt>

<span id="REMOTE_HOST"></span><span id="remote_host"></span>REMOTE\_HOST
</dt> <dd>

The host name of the client.

</dd> <dt>

<span id="REMOTE_USER"></span><span id="remote_user"></span>REMOTE\_USER
</dt> <dd>

This contains the user name supplied by the client and authenticated by the server.

</dd> <dt>

<span id="REQUEST_METHOD"></span><span id="request_method"></span>REQUEST\_METHOD
</dt> <dd>

The HTTP request method.

</dd> <dt>

<span id="SCRIPT_NAME"></span><span id="script_name"></span>SCRIPT\_NAME
</dt> <dd>

The name of the script program being run.

</dd> <dt>

<span id="SERVER_NAME"></span><span id="server_name"></span>SERVER\_NAME
</dt> <dd>

The server’s host name (or IP address) as it should appear in self-referencing URLs.

</dd> <dt>

<span id="SERVER_PORT"></span><span id="server_port"></span>SERVER\_PORT
</dt> <dd>

The TCP/IP port on which the request was received.

</dd> <dt>

<span id="SERVER_PROTOCOL"></span><span id="server_protocol"></span>SERVER\_PROTOCOL
</dt> <dd>

The name and version of the information-retrieval protocol relating to this request, usually HTTP 1.0.

</dd> <dt>

<span id="SERVER_SOFTWARE"></span><span id="server_software"></span>SERVER\_SOFTWARE
</dt> <dd>

The name and version of the web server under which the Internet Server Extension is running.

</dd> </dl>

 

 




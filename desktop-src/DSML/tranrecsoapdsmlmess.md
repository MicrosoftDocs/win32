---
title: Transmitting and Receiving SOAP-DSML Messages
description: DSML Services for Windows implements SOAP through HTTP binding.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 28bc6aa1-82a0-4484-b61f-02138157252b
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Transmitting and Receiving SOAP-DSML Messages DSML
- DSML Services for Windows, transmitting messages
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Transmitting and Receiving SOAP-DSML Messages

DSML Services for Windows implements SOAP through HTTP binding.

The following code example shows how to configure a webpage that employs server-side scripting to enable a client to transmit and receive SOAP-DSML messages. This webpage code is common to each of the LDAP-operations topics that follow. Therefore, only the webpage code will be discussed here, and the SOAP-DSML code will be discussed separately in topics that follow.

In the following example, the SOAP envelope that contains the DSML payload is sent from the server to the client, and from the client to the server over HTTP. This process is accomplished by creating a webpage that imports the SOAP envelope and its payload into a form, displays it, and then transmits it to the server by using Visual Basic Scripting Edition (VBScript) to perform an HTML POST operation. The following code example shows how this process works.


```VB
<html>
 <script language="VBScript">
sub postit(theform)
    set xmlhttp = CreateObject("Msxml2.XMLHTTP")
    xmlhttp.open "POST", "http://localhost/dsmlsoap/adssoap.dsmlx", false
    xmlhttp.setRequestHeader "SOAPAction", """#batchRequest"""
    xmlhttp.send theform.requestEl.value
    theform.responseEl.value = xmlhttp.responsetext
end sub

sub LoadDoc()
    set dom = CreateObject("Microsoft.XMLDOM")
    dom.async = False
    path = Mid(Location.Search,2)
    dom.Load path
    myform.requestEl.value = dom.Xml
end sub

 </script>

 <body OnLoad="LoadDoc">

  <form name="myform" METHOD=POST ACTION="http://localhost/dsmlsoap/adssoap.dsmlx" >

   <img border="0" src="sample.JPG" width="89" height="92"/> 
   <img border="0" src="dsmlsoap.jpg" width="435" height="47"/>
   <p><font face="Verdana" size="2">DSML 2.0 request: </font></p>
   <p><textarea fontsize="large" rows="10" cols=110 name="requestEl">
    </textarea></p>
   <input type="button" Value="Send Request" OnClick="postit(myform)">
   <p><font face="Verdana" size="2">The DSML 2.0 response: </font></p>

   <textarea rows="20" cols=110 name="responseEl">
   </textarea>


   <object id="ResponseXML" width="900" height="300" classid="CLSID:8856F961-340A-11D0-A96B-00C04FD705A2">
   </object>


  </form>
 </body>
</html>
```



This webpage code creates a form named `myform` and, through the VBScript subroutine **LoadDoc()**, creates a **DOMDocument** object and, using this object, loads a SOAP message that contains the DSML payload. The **Mid** function is used in conjunction with the **Location.Search** method to get the path to the file Add.xml, which contains the SOAP and DSML XML elements. This path is then used to load and display the XML payload and to include the XML code in the HTTP request. A real-life application would probably collect data from the user and then create the SOAP and DSML elements using this information.

The form also contains a Send Request button that, when clicked, calls the Visual Basic subroutine **postit**, and which passes the argument *myform*. The **postit** subroutine then posts the HTTP request to the server.

The **postit** subroutine creates an **IXMLHTTPRequest** object named `xmlhttp`. The **Open** method is used to configure the necessary POST data. In this example, the data includes the URL to Adssoap.dll and the synchronous operation setting. Next, the request header data is configured using the **setRequestHeader** method. Then the **Send** method is used to send the request to the server.

 

 





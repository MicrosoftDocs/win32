---
title: Using VBScript
description: Using VBScript
ms.assetid: a078eb60-aa12-42ea-850c-7b845fc8037c
ms.topic: article
ms.date: 05/31/2018
---

# Using VBScript

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

VBScript is a programming language included with Microsoft Internet Explorer. For other browsers, contact your vendor about support. VBScript 2.0 (or later) is recommended for use with Agent. Although earlier versions of VBScript may work with Agent, they lack certain functions that you may want to use. You can download VBScript 2.0 and obtain further information on VBScript at the Microsoft Downloads site and the Microsoft VBScript site.

To program Microsoft Agent from VBScript, use the HTML &lt;SCRIPT&gt; tags. To access the programming interface, use the name of control you assign in the &lt;OBJECT&gt; tag, followed by the subobject (if any), the name of the method or property, and any parameters or values supported by the method or property:

``` syntax
agent[.object].Method parameter, [parameter]
agent[.object].Property = value
```

For events, include the name of the control followed by the name of the event and any parameters:

``` syntax
Sub agent_event (ByVal parameter[,ByVal parameter])
statements
End Sub
```

You can also specify an event handler using the &lt;SCRIPT&gt; tag's **For...Event** syntax:

``` syntax
<SCRIPT LANGUAGE=VBScript For=agent Event=event[(parameter[,parameter])]>
statements
</SCRIPT>
```

Although Microsoft Internet Explorer supports this latter syntax, not all browsers do. For compatibility, use only the former syntax for events.

With VBScript (2.0 or later), you can verify whether Microsoft Agent is installed by trying to create the object and checking to see if it exists. The following sample demonstrates how to check for the Agent control without triggering an auto-download of the control (as would happen if you included an &lt;OBJECT&gt; tag for the control on the page):

``` syntax
<!-- WARNING - This code requires VBScript 2.0.
It will always fail to detect the Agent control
in VbScript 1.x, because CreateObject doesn't work.
-->

<SCRIPT LANGUAGE=VBSCRIPT>
If HaveAgent() Then
      'Microsoft Agent control was found.
document.write "<H2 align=center>Found</H2>"
Else
      'Microsoft Agent control was not found.
document.write "<H2 align=center>Not Found</H2>"
End If

Function HaveAgent()
' This procedure attempts to create an Agent Control object.
' If it succeeds, it returns True.
'    This means the control is available on the client.
' If it fails, it returns False.
'    This means the control hasn't been installed on the client.

   Dim agent
   HaveAgent = False
   On Error Resume Next
   Set agent = CreateObject("Agent.Control.1")
   HaveAgent = IsObject(agent)

End Function

</SCRIPT>
```

 

 





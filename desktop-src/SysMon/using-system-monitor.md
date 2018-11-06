---
title: Using System Monitor
description: System Monitor (SYSMON) can be included in any application that supports ActiveX \ 174; controls. For example, you can include SYSMON in a Microsoft Visual Basic application or in an HTML document.
ms.assetid: 36931aae-b608-42d9-a3e3-09784e80f386
ms.topic: article
ms.date: 05/31/2018
---

# Using System Monitor

System Monitor (SYSMON) can be included in any application that supports ActiveX® controls. For example, you can include SYSMON in a Microsoft Visual Basic application or in an HTML document.

The following example shows how to include SYSMON in an HTML document. The example uses VBScript to add counters whose values are retrieved from the local computer, modifies some of the SYSMON properties that control how the monitor is displayed, and processes the OnCounterAdd event. The example uses the wildcard character (\*) to add all instances of the process counter.

``` syntax
<HTML>
<BODY BGCOLOR=#C0C0C0>

<SCRIPT LANGUAGE="VBScript">
  Sub Monitor_OnCounterAdded(index)
    Monitor.Counters.Item(1).Width = 8
  End Sub
</Script>
<OBJECT
  CLASSID="clsid:C4D2D8E0-D1DD-11CE-940F-008029004347"
  ID="Monitor"
  HEIGHT=80%
  WIDTH=100%>
</OBJECT>

<SCRIPT LANGUAGE="VBScript">
  Sub Window_OnLoad
    On Error Resume Next
    Monitor.ShowValueBar = False
    Monitor.ShowHorizontalGrid = True
    Monitor.Counters.Add("\Process(*)\% Processor Time")
    Monitor.DisplayType=sysmonLineGraph
    Monitor.GraphTitle="System Performance Overview"
  End Sub
</SCRIPT>

</BODY>
</HTML>
```

 

 





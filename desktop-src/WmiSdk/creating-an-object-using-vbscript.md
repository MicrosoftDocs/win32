---
description: You can create an object for WMI in Visual Basic Scripting Edition (VBScript) by connecting to WMI and then calling CreateObject. The following table lists the methods in the Scripting API for WMI that support object creation.
ms.assetid: 3acbce31-6d56-4a7a-af03-fa37b2b868be
ms.tgt_platform: multiple
title: Creating an Object Using VBScript
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Creating an Object Using VBScript

You can create an object for WMI in Visual Basic Scripting Edition (VBScript) by connecting to WMI and then calling [CreateObject](/previous-versions//xzysf6hc(v=vs.85)). The following table lists the methods in the Scripting API for WMI that support object creation.



| Interface                                        | ProgID                             |
|--------------------------------------------------|------------------------------------|
| [**SWbemDateTime**](swbemdatetime.md)           | "WbemScripting.SwbemDateTime"      |
| [**SWbemLocator**](swbemlocator.md)             | "WbemScripting.SWbemLocator"       |
| [**SWbemLastError**](swbemlasterror.md)         | "WbemScripting.SWbem.LastError"    |
| [**SWbemObjectPath**](swbemobjectpath.md)       | "WbemScripting.SWbemObjectPath"    |
| [**SWbemNamedValueSet**](swbemnamedvalueset.md) | "WbemScripting.SWbemNamedValueSet" |
| [**SWbemRefresher**](swbemrefresher.md)         | "WbemScripting.SWbemRefresher"     |
| [**SWbemSink**](swbemsink.md)                   | "WbemScripting.SWbemSink"          |



 

The following procedure describes how to create a WMI object using VBScript.

**To create a WMI object using VBScript**

1.  Connect to WMI using either a moniker or an [**SWbemLocator**](swbemlocator.md) object.

    For more information, see [Creating a WMI Script](creating-a-wmi-script.md).

2.  Make a call to the VBScript [CreateObject](/previous-versions//xzysf6hc(v=vs.85)) method.

    The following code example shows how to create an object.

    ```VB
    Set locator = CreateObject("WbemScripting.SWbemLocator")
    ```

    

    If you use a moniker in Step 1, you do not need to call [CreateObject](/previous-versions//xzysf6hc(v=vs.85)) again.

 

 

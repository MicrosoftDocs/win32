---
description: Provides extended functionality for SWbemObject. Like SWbemObject, the methods of this extended object can be used by all WMI objects.
ms.assetid: 944d4cdc-ad35-4b53-b755-f10131a087fb
ms.tgt_platform: multiple
title: SWbemObjectEx object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObjectEx
- SetFromText_
- ISWbemObjectEx
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObjectEx object

The **SWbemObjectEx** object provides extended functionality for [**SWbemObject**](swbemobject.md). Like **SWbemObject**, the methods of this extended object can be used by all WMI objects. This object cannot be created by the VBScript [CreateObject](/previous-versions//xzysf6hc(v=vs.85)) call.

## Members

The **SWbemObjectEx** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemObjectEx** object has these methods.



| Method                                      | Description                                                              |
|:--------------------------------------------|:-------------------------------------------------------------------------|
| [**GetText\_**](swbemobjectex-gettext-.md) | Returns a text file showing the contents of an object in XML.<br/> |
| [**Refresh\_**](swbemobjectex-refresh-.md) | Refreshes data in an object.<br/>                                  |
| **SetFromText\_**                           | Reserved for future use.<br/>                                      |



 

### Properties

The **SWbemObjectEx** object has these properties.



| Property                                                                 | Access type           | Description                                                                                                                                              |
|:-------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SystemProperties\_**](swbemobjectex-systemproperties-.md)<br/> | Read/write<br/> | An [**SWbemPropertySet**](swbempropertyset.md) object that contains the collection of system properties that apply to the **SWbemObjectEx**.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemObjectEx<br/>                                                         |
| IID<br/>                      | IID\_ISWbemObjectEx<br/>                                                          |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> <dt>

[**SWbemObject**](swbemobject.md)
</dt> <dt>

[WbemObjectTextFormatEnum](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemobjecttextformatenum)
</dt> </dl>

 


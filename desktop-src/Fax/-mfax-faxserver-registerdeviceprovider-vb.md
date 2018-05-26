---
Description: The RegisterDeviceProvider method registers a fax service provider (FSP) with the fax service. Registration takes place after the fax service restarts.
ms.assetid: 04cbf53b-2fc5-4f7a-8430-988b5cfa8f52
title: FaxServer.RegisterDeviceProvider method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxServer.RegisterDeviceProvider method

The **RegisterDeviceProvider** method registers a fax service provider (FSP) with the fax service. Registration takes place after the fax service restarts.

## Syntax


```VB
FaxServer.RegisterDeviceProvider( _
  ByVal bstrGUID As String, _
  ByVal bstrFriendlyName As String, _
  ByVal bstrImageName As String, _
  ByVal bstrTempName As String, _
  ByVal lFSPIVersion As Long _
) As Long
```



## Parameters

<dl> <dt>

*bstrGUID* 
</dt> <dd>

Type: **String**

Null-terminated string that contains the GUID that uniquely identifies the FSP that is registering.

</dd> <dt>

*bstrFriendlyName* 
</dt> <dd>

Type: **String**

Null-terminated string that contains the user-friendly name to display for the FSP that is registering.

</dd> <dt>

*bstrImageName* 
</dt> <dd>

Type: **String**

Null-terminated string that contains the fully qualified path and file name of the FSP DLL.

</dd> <dt>

*bstrTempName* 
</dt> <dd>

Type: **String**

Null-terminated string that contains the name of the telephony service provider associated with the devices for the FSP.

</dd> <dt>

*lFSPIVersion* 
</dt> <dd>

Type: **Long**

A **Long** value that indicates the version of the FSP. Should be equal to 0x00010000.

</dd> </dl>

## Remarks

Only an administrator can register a FSP.

To use this method, a user must have the [**farMANAGE\_CONFIG**](/windows/previous-versions/FaxComex/ne-faxcomex-fax_access_rights_enum?branch=master) access right.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>FaxComex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |



## See also

<dl> <dt>

[**FaxServer**](-mfax-faxserver.md)
</dt> <dt>

[**IFaxServer**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxserver?branch=master)
</dt> </dl>

 

 





---
Description: The RegisterInboundRoutingExtension method registers a fax inbound routing extension with the fax service. Registration takes place after the fax service restarts.
ms.assetid: d4edf767-32bc-4d44-af19-3ae63d68cffa
title: FaxServer.RegisterInboundRoutingExtension method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxServer.RegisterInboundRoutingExtension method

The **RegisterInboundRoutingExtension** method registers a fax inbound routing extension with the fax service. Registration takes place after the fax service restarts.

## Syntax


```VB
FaxServer.RegisterInboundRoutingExtension( _
  ByVal bstrExtensionName As String, _
  ByVal bstrFriendlyName As String, _
  ByVal bstrImageName As String, _
  ByVal vMethods As Variant _
) As Long
```



## Parameters

<dl> <dt>

*bstrExtensionName* 
</dt> <dd>

Type: **String**

String that specifies the internal name of the fax routing extension DLL.

</dd> <dt>

*bstrFriendlyName* 
</dt> <dd>

Type: **String**

String to associate with the fax routing extension DLL. This is the routing extension's user-friendly name, suitable for display.

</dd> <dt>

*bstrImageName* 
</dt> <dd>

Type: **String**

String that specifies the full path and file name for the fax routing extension DLL. The path can include valid environment variables, for example, %SYSTEMDRIVE% and %SYSTEMROOT%.

</dd> <dt>

*vMethods* 
</dt> <dd>

Type: **Variant**

[VARIANT](e305240e-9e11-4006-98cc-26f4932d2118) that specifies a safearray of **String**s. The array must be unidimensional, it cannot be empty, and it must have a lower limit of zero. Each item (string) in the array must identify a routing method. The string must have the following format: Method name; Friendly name; Function Name; Method GUID

</dd> </dl>

## Remarks

Only an administrator can register a routing extension. Also, this method works only on the local fax server.

This property is not supported in Windows XP, and will return the error: [FAX\_E\_NOT\_SUPPORTED\_ON\_THIS\_SKU](-mfax-fax-error-codes.md).

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

 

 





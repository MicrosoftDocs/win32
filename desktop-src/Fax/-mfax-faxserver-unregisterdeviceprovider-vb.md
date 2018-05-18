---
Description: 'The UnregisterDeviceProvider method unregisters (removes the registration of) an existing device provider. Unregistration will take place only after the fax server is restarted.'
ms.assetid: '4379a7ca-eeef-4a83-823c-aeb57f3eed42'
title: 'FaxServer.UnregisterDeviceProvider method'
---

# FaxServer.UnregisterDeviceProvider method

The **UnregisterDeviceProvider** method unregisters (removes the registration of) an existing device provider. Unregistration will take place only after the fax server is restarted.

## Syntax


```VB
FaxServer.UnregisterDeviceProvider( _
  ByVal bstrUniqueName As String _
) As Long
```



## Parameters

<dl> <dt>

*bstrUniqueName* 
</dt> <dd>

Type: **String**

Required. Specifies the unique name that identifies the FSP that is unregistering.

</dd> </dl>

## Remarks

Only an administrator can unregister a fax service provider.

To use this method, a user must have the [**farMANAGE\_CONFIG**](-mfax-fax-access-rights-enum.md) access right.

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

[**IFaxServer**](-mfax-faxserver-cpp.md)
</dt> </dl>

 

 





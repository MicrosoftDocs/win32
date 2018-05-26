---
Description: The Clear method clears the application protocol data unit (APDU) and reply APDU message buffers.
ms.assetid: 5fd3ebb9-b492-4668-9dd8-3ffbcfceb12c
title: ISCardCmdClear method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISCardCmd::Clear method

\[The **Clear** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](secsmart.smart_card_modules) provide similar functionality.\]

The **Clear** method clears the [*application protocol data unit*](security.a_gly#-security-application-protocol-data-unit-gly) (APDU) and [*reply APDU*](security.r_gly#-security-reply-apdu-gly) message buffers.

## Syntax


```C++
HRESULT Clear();
```



## Parameters

This method has no parameters.

## Return value

The method returns one of the following possible values.



| Return code                                                                             | Description                                  |
|-----------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Operation completed successfully.<br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Unknown error.<br/>                    |



 

## Remarks

To build a command APDU, call [**BuildCmd**](iscardcmd-buildcmd.md).

For a list of all the methods provided by this interface, see [**ISCardCmd**](iscardcmd.md).

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md#smart-card-return-values).

## Examples

The following example shows how to clear the APDU and reply APDU message buffers.


```C++
HRESULT  hr;

hr = pISCardCmd->Clear();
if (FAILED(hr))
{
    printf("Failed ISCardCmd::Clear\n");
    // Take other error handling action as needed.
}
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scarddat.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scarddat.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCardCmd is defined as D5778AE3-43DE-11D0-9171-00AA00C18068<br/>            |



## See also

<dl> <dt>

[**ISCardCmd::BuildCmd**](iscardcmd-buildcmd.md)
</dt> <dt>

[**ISCardCmd**](iscardcmd.md)
</dt> </dl>

 

 





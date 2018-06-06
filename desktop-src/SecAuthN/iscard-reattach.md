---
Description: The ReAttach method resets, or reinitializes, the smart card.
ms.assetid: c9cd9cd7-5ee6-48dc-8460-deb9c827fcc4
title: ISCard::ReAttach method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISCard::ReAttach method

\[The **ReAttach** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](https://msdn.microsoft.com/a33e4e23-5f0d-4d03-ae3b-8727cdf57ab7) provide similar functionality.\]

The **ReAttach** method resets, or reinitializes, the [*smart card*](security.s_gly#-security-smart-card-gly).

## Syntax


```C++
HRESULT ReAttach(
  [in] SCARD_SHARE_MODES  ShareMode,
  [in] SCARD_DISPOSITIONS InitState
);
```



## Parameters

<dl> <dt>

*ShareMode* \[in\]
</dt> <dd>

Mode in which to share or exclusively own the connection to the smart card.



| Value                                                                                                                                            | Meaning                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <span id="EXCLUSIVE"></span><span id="exclusive"></span><dl> <dt>**EXCLUSIVE**</dt> </dl> | No one else use this connection to the smart card.<br/> |
| <span id="SHARED"></span><span id="shared"></span><dl> <dt>**SHARED**</dt> </dl>          | Other applications can use this connection.<br/>        |



 

</dd> <dt>

*InitState* \[in\]
</dt> <dd>

Indicates what to do with the card.



| Value                                                                                                                                      | Meaning                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| <span id="LEAVE"></span><span id="leave"></span><dl> <dt>**LEAVE**</dt> </dl>       | Leaves the smart card in the current [*state*](security.s_gly#-security-state-gly).<br/> |
| <span id="RESET"></span><span id="reset"></span><dl> <dt>**RESET**</dt> </dl>       | Resets the smart card to some known state.<br/>                                                              |
| <span id="UNPOWER"></span><span id="unpower"></span><dl> <dt>**UNPOWER**</dt> </dl> | Removes power from the smart card.<br/>                                                                      |
| <span id="EJECT"></span><span id="eject"></span><dl> <dt>**EJECT**</dt> </dl>       | Ejects the smart card if the reader has eject capabilities.<br/>                                             |



 

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                  | Description                                                                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Operation completed successfully.<br/>                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | There is something wrong with one or more of the parameters passed into the function.<br/> |



 

## Remarks

In addition to the COM error codes listed above, this interface may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md#smart-card-return-values).

## Examples

The following example shows reinitializing the smart card.


```C++
HRESULT    hr;

// Reattach the smart card.
hr = pISCard->ReAttach(SHARED, LEAVE);
if (FAILED(hr))
{
   printf("Failed ReAttach\n");
   // Take error handling action as needed.
}
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardmgr.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardmgr.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCard is defined as 1461AAC3-6810-11D0-918F-00AA00C18068<br/>               |



## See also

<dl> <dt>

[**AttachByHandle**](iscard-attachbyhandle.md)
</dt> <dt>

[**AttachByReader**](iscard-attachbyreader.md)
</dt> <dt>

[**Detach**](iscard-detach.md)
</dt> <dt>

[**ISCard**](iscard.md)
</dt> </dl>

 

 





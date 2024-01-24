---
description: Retrieves the node address (Nad) used by the smart card in the reply message.
ms.assetid: bf4f281c-d378-4abd-8f2e-e23c2f4e87a4
title: ISCardCmd::get_ReplyNad method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardCmd.get_ReplyNad
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardCmd::get\_ReplyNad method

\[The **get\_ReplyNad** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **get\_ReplyNad** method retrieves the node address (Nad) used by the [*smart card*](../secgloss/s-gly.md) in the reply message.

## Syntax


```C++
HRESULT get_ReplyNad(
  [out] BYTE *pbNad
);
```



## Parameters

<dl> <dt>

*pbNad* \[out\]
</dt> <dd>

Pointer to the byte that contains the Nad used by the reply message, on return.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                    | Description                                                        |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>           | Operation was completed successfully.<br/>                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>   | The *pbNad* parameter is not valid.<br/>                     |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl> | Internal calls were unable to retrieve Nad information.<br/> |



 

## Remarks

In addition to the COM error codes listed above, this method may return a smart card error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Examples

The following example shows how to retrieve the node address (Nad) used by the [*smart card*](../secgloss/s-gly.md) in the reply message. The example assumes that pISCardCmd is a valid pointer to an instance of the [**ISCardCmd**](iscardcmd.md) interface.


```C++
BYTE    byNad;
HRESULT hr;

// Get reply Nad.
hr = pISCardCmd->get_ReplyNad(&byNad);
if (FAILED(hr))
{
  printf("Failed get_ReplyNad\n");
  // Take other error handling action as needed.
}
```



## Requirements



| Requirement | Value |
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

[**ISCardCmd**](iscardcmd.md)
</dt> </dl>

 

 

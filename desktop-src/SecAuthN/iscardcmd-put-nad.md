---
description: Specifies the node address (Nad) to use with the ISCardCmd interface.
ms.assetid: 49de8264-9491-41a4-a8e0-68d0db088ded
title: ISCardCmd::put_Nad method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardCmd.put_Nad
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardCmd::put\_Nad method

\[The **put\_Nad** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **put\_Nad** method specifies the node address (Nad) to use with the [**ISCardCmd**](iscardcmd.md) interface. This applies to communications using the [*T=1 protocol*](../secgloss/t-gly.md) communications only. By default, the [**ISCardCmd**](iscardcmd.md) object uses a Nad of zero.

## Syntax


```C++
HRESULT put_Nad(
  [in] BYTE bNad
);
```



## Parameters

<dl> <dt>

*bNad* \[in\]
</dt> <dd>

Byte representing the Nad to use.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                  | Description                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Operation was completed successfully.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *bNad* parameter is not valid.<br/>    |



 

## Remarks

This method should be called only when it is necessary to use a value other than zero for the Nad.

## Examples

The following example shows how to specify a node address to use with the [**ISCardCmd**](iscardcmd.md) interface. The example assumes that byNadValue is a variable of type **BYTE** that was previously assigned a value, and that pISCardCmd is a valid pointer to an instance of the **ISCardCmd** interface.


```C++
HRESULT  hr;

// Set the Nad.
// byNadValue is a previously assigned BYTE value.
hr = pISCardCmd->put_Nad(byNadValue);
if (FAILED(hr))
{
  printf("Failed put_Nad\n");
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

 

 

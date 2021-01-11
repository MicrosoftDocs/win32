---
description: Sets the given instruction identifier in the application protocol data unit (APDU).
ms.assetid: ea527ffd-b053-467d-883d-b93d5bbfb071
title: ISCardCmd::put_InstructionId method (Scarddat.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardCmd.put_InstructionId
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardCmd::put\_InstructionId method

\[The **put\_InstructionId** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **put\_InstructionId** method sets the given instruction identifier in the [*application protocol data unit*](../secgloss/a-gly.md) (APDU).

## Syntax


```C++
HRESULT put_InstructionId(
  [in] BYTE byIns
);
```



## Parameters

<dl> <dt>

*byIns* \[in\]
</dt> <dd>

The byte that is the instruction identifier.

</dd> </dl>

## Return value

The method returns one of the following possible values.



| Return code                                                                                   | Description                                    |
|-----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Operation completed successfully.<br/>   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | The *byIns* parameter is not valid.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Out of memory.<br/>                      |



 

## Remarks

To get the existing instructional identifier, call [**get\_InstructionId**](iscardcmd-get-instructionid.md).

For a list of all the methods provided by this interface, see [**ISCardCmd**](iscardcmd.md).

In addition to the COM error codes listed above, this interface may return a [*smart card*](../secgloss/s-gly.md) error code if a smart card function was called to complete the request. For more information, see [Smart Card Return Values](authentication-return-values.md).

## Examples

The following example shows how to set an instruction identifier in the [*application protocol data unit*](../secgloss/a-gly.md) (APDU). The example assumes that pISCardCmd is a valid pointer to an instance of the [**ISCardCmd**](iscardcmd.md) interface.


```C++
HRESULT hr;

// Set the instruction ID.
hr = pISCardCmd->put_InstructionId(0xb2);
if (FAILED(hr))
{
  printf("Failed put_InstructionId\n");
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

[**get\_InstructionId**](iscardcmd-get-instructionid.md)
</dt> <dt>

[**ISCardCmd**](iscardcmd.md)
</dt> </dl>

 

 

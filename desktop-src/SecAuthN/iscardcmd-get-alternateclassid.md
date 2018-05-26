---
Description: Retrieves the value of the alternate class ID.
ms.assetid: 80c7cbba-e28d-4973-9f3f-7636ff331b64
title: ISCardCmdget\_AlternateClassId method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISCardCmd::get\_AlternateClassId method

\[The **get\_AlternateClassId** method is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](secsmart.smart_card_modules) provide similar functionality.\]

The **get\_AlternateClassId** method retrieves the value of the alternate class ID. This method will fail unless the alternate ID has been set by a previous call to [**put\_AlternateClassId**](iscardcmd-put-alternateclassid.md).

## Syntax


```C++
HRESULT get_AlternateClassId(
  [out] BYTE *pbyClass
);
```



## Parameters

<dl> <dt>

*pbyClass* \[out\]
</dt> <dd>

Pointer to the byte that contains the alternate class ID value on return.

</dd> </dl>

## Return value

The method returns the following possible values.



| Return code                                                                                    | Description                                                                                                                                 |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>           | Operation was completed successfully.<br/>                                                                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>   | The *pbyClass* parameter is not valid.<br/>                                                                                           |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl> | The alternate class ID has not been previously set by a call to [**put\_AlternateClassId**](iscardcmd-put-alternateclassid.md).<br/> |



 

## Remarks

This method applies to communications using the [*T=0 protocol*](security.t_gly#-security-t-0-protocol-gly). For more information, see [**put\_AlternateClassId**](iscardcmd-put-alternateclassid.md).

## Examples

The following example shows how to retrieve the alternate class ID. The example assumes that pISCardCmd is a valid pointer to an instance of the [**ISCardCmd**](iscardcmd.md) interface.


```C++
BYTE     byAltClassID;
HRESULT  hr;

// Retrieve the alternate class ID.
hr = pISCardCmd->get_AlternateClassId(&amp;byAltClassID);
if (FAILED(hr))
{
  printf("Failed get_AltClassId\n");
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

[**ISCardCmd**](iscardcmd.md)
</dt> <dt>

[**put\_AlternateClassId**](iscardcmd-put-alternateclassid.md)
</dt> </dl>

 

 





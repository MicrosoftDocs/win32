---
error-parsing-yaml: 
---

# IVMMouse::GetButton method

The **GetButton** method returns the current state (up or down) of the specified mouse button.

## Syntax


```C++
HRESULT GetButton(
  [in]  VMMouseButton buttonIndex,
  [out] VARIANT_BOOL  *isDown
);
```



## Parameters

<dl> <dt>

*buttonIndex* \[in\]
</dt> <dd>

The enumerated index of the button whose state is being requested.

</dd> <dt>

*isDown* \[out\]
</dt> <dd>

The state of the indicated button. **TRUE** if the button is currently down in the virtual machine.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                | Description                                                                                     |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>                     | The operation was successful.<br/>                                                        |
| <dl> <dt> **E\_POINTER** </dt> </dl>                | The *isDown* parameter is **NULL**.<br/>                                                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | The *buttonIndex* parameter is not valid.<br/>                                            |
| <dl> <dt> **VM\_E\_VM\_NOT\_RUNNING** </dt> </dl>   | The virtual machine to which this mouse device is attached is not currently running.<br/> |
| <dl> <dt> **VM\_E\_MOUSE\_NOT\_ACTIVE** </dt> </dl> | The mouse device has not been powered up.<br/>                                            |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl>        | An unexpected error occurred.<br/>                                                        |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMMouse**](ivmmouse.md)
</dt> <dt>

[**VMMouseButton**](vmmousebutton.md)
</dt> </dl>

 

 






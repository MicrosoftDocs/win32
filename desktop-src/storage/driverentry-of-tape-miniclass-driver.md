---
title: DriverEntry of Tape Miniclass Driver routine
description: DriverEntry initializes a tape miniclass driver. This routine is required.
ms.assetid: 'dc082f31-5ec5-491e-a347-8f8e485c042b'
keywords: ["DriverEntry routine Storage Devices"]
topic_type:
- apiref
api_name:
- DriverEntry
api_location:
- NtosKrnl.exe
api_type:
- DllExport
---

# DriverEntry of Tape Miniclass Driver routine

**DriverEntry** initializes a tape miniclass driver. This routine is required.

## Syntax


```C++
ULONG DriverEntry(
  _In_ PVOID Argument1,
  _In_ PVOID Argument2
);
```



## Parameters

<dl> <dt>

*Argument1* \[in\]
</dt> <dd>

Pointer to a driver context that a tape miniclass driver passes to [**TapeClassInitialize**](tapeclassinitialize.md). The format of the context information is OS-specific and must not be interpreted by portable tape miniclass drivers.

</dd> <dt>

*Argument2* \[in\]
</dt> <dd>

Pointer to a second context structure that a tape miniclass driver passes to **TapeClassInitialize**. The format of the context information is OS-specific and must not be interpreted by portable tape miniclass drivers.

</dd> </dl>

## Return value

**DriverEntry** returns the value returned by its call to **TapeClassInitialize**.

## Remarks

**DriverEntry** is the initial entry point for a tape miniclass driver.

Since **TapeClassInitialize** performs most of the required driver initialization, the primary task of a tape miniclass driver's **DriverEntry** routine is to allocate and fill in a TAPE\_INIT\_DATA\_EX structure with driver-specific constants and entry points.

**DriverEntry** first must call [**TapeClassZeroMemory**](tapeclasszeromemory.md) to clear the TAPE\_INIT\_DATA\_EX structure. **DriverEntry** then sets the values and pointers in the structure.

**DriverEntry** calls **TapeClassInitialize** and passes the address of TAPE\_INIT\_DATA\_EX and the two pointers that were passed to **DriverEntry** (*Argument1* and *Argument2*). **TapeClassInitialize** completes driver initialization and returns status to the tape miniclass driver's **DriverEntry** routine. **DriverEntry** returns the status that it received from **TapeClassInitialize**.

## Requirements



|                            |                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>      |
| Header<br/>          | <dl> <dt>Minitape.h</dt> </dl>   |
| Library<br/>         | <dl> <dt>NtosKrnl.lib</dt> </dl> |
| DLL<br/>             | <dl> <dt>NtosKrnl.exe</dt> </dl> |



## See also

<dl> <dt>

[**TAPE\_INIT\_DATA\_EX**](tape-init-data-ex.md)
</dt> <dt>

[**TapeClassInitialize**](tapeclassinitialize.md)
</dt> <dt>

[**TapeClassZeroMemory**](tapeclasszeromemory.md)
</dt> <dt>

[**TAPE\_STATUS**](tape-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DriverEntry%20of%20Tape%20Miniclass%20Driver%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







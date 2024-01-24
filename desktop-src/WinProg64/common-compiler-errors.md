---
title: Common Compiler Errors
description: This section illustrates the typical compiler errors that occur when migrating an existing code base. These examples happen to be from system-level HAL code, although the concepts are directly applicable to user-level code.
ms.assetid: bbb6a57f-281a-4a6e-a4b6-15846d0cf21f
keywords:
- compiler errors 64-bit Windows Programming
- migration 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Common Compiler Errors

This section illustrates the typical compiler errors that occur when migrating an existing code base. These examples happen to be from system-level HAL code, although the concepts are directly applicable to user-level code.

## Warning C4311 Example 1

'type cast' : pointer truncation from 'void \*\_\_ptr64 ' to 'unsigned long

<dl> <dt>

<span id="Code"></span><span id="code"></span><span id="CODE"></span>Code
</dt> <dd>

`pPciAddr->u.AsULONG = (ULONG) CIA_PCI_CONFIG_BASE_QVA;`

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

**PtrToUlong** is an inline function or macro, depending on your usage. It truncates a pointer to a **ULONG**. Although 32-bit pointers are not affected, the upper half of a 64-bit pointer is truncated.

CIA\_PCI\_CONFIG\_BASE\_QVA is declared as a **PVOID**. The **ULONG** cast works in the 32-bit world, but results in an error in the 64-bit world. The solution is to get a 64-bit pointer to a **ULONG**, because changing the definition of the union that pPciAddr->u.AsULONG is defined in changes too much code.

Using the macro **PtrToUlong** to convert the 64-bit **PVOID** to the needed **ULONG** is allowed because we have knowledge about the specific value of CIA\_PCI\_CONFIG\_BASE\_QVA. In this case, this pointer will never have data in the upper 32 bits.

</dd> <dt>

<span id="Solution"></span><span id="solution"></span><span id="SOLUTION"></span>Solution
</dt> <dd>

`pPciAddr->u.AsULONG = PtrToUlong(CIA_PCI_CONFIG_BASE_QVA);`

</dd> </dl>

## Warning C4311 Example 2

'type cast' : pointer truncation from 'struct \_ERROR\_FRAME \*\_\_ptr64 ' to 'unsigned long

<dl> <dt>

<span id="Code"></span><span id="code"></span><span id="CODE"></span>Code
</dt> <dd>

`KeBugCheckEx( DATA_BUS_ERROR,0,0,0,(ULONG)PUncorrectableError );`

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

The problem is that the last parameter to this function is a pointer to a data structure. Because PUncorrectableError is a pointer, it changes size with the programming model. The prototype for **KeBugCheckEx** was changed so that the last parameter is a **ULONG\_PTR**. As a result, it's necessary to cast the function pointer to a **ULONG\_PTR**.

You might ask why **PVOID** was not used as the last parameter. Depending on the context of the call, the last parameter may be something other than a pointer or perhaps an error code.

</dd> <dt>

<span id="Solution"></span><span id="solution"></span><span id="SOLUTION"></span>Solution
</dt> <dd>

`KeBugCheckEx( DATA_BUS_ERROR,0,0,0,(ULONG_PTR)PUncorrectableError );`

</dd> </dl>

## Warning C4244 Example 1

'=' : conversion from 'struct \_CONFIGURATION\_COMPONENT \*\_\_ptr64 ' to 'struct \_CONFIGURATION\_COMPONENT \*', possible loss of data

<dl> <dt>

<span id="Code"></span><span id="code"></span><span id="CODE"></span>Code
</dt> <dd>

`Component = &CurrentEntry->ComponentEntry;`

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

The function declares the variable Component as a PCONFIGURATION\_COMPONENT. Later, the variable is used in the following assignment that appears correct:

`Component = &CurrentEntry->ComponentEntry;`

However, the type PCONFIGURATION\_COMPONENT is defined as:

``` syntax
typedef struct __CONFIGURATION_COMPONENT {
...
...
} CONFIGURATION_COMPONENT, * POINTER_32 PCONFIGURATION_COMPONENT;
```

The type definition for PCONFIGURATION\_COMPONENT provides a 32-bit pointer in both 32-bit and 64-bit models because it is declared **POINTER\_32**. The original designer of this structure knew it was going to be used in a 32-bit context in the BIOS and expressly defined it for that use. This code works fine in 32-bit Windows because the pointers happen to be 32-bit. In 64-bit Windows, it does not work because the code is in 64-bit context.

</dd> <dt>

<span id="Solution"></span><span id="solution"></span><span id="SOLUTION"></span>Solution
</dt> <dd>

To work around this problem, use CONFIGURATION\_COMPONENT \* rather than the 32-bit PCONFIGURATION\_COMPONENT . It is important to clearly understand the purpose of the code. If this code is intended to touch 32-bit BIOS or System space, this fix will not work.

**POINTER\_32** is defined in Ntdef.h and Winnt.h.

``` syntax
#ifdef (__AXP64__)
#define POINTER_32 _ptr32
#else
#define POINTER_32
#endif
```

</dd> </dl>

## Warning C4242 Example 2

'=' : conversion from '\_\_int64 ' to 'unsigned long ', possible loss of data

<dl> <dt>

<span id="Code"></span><span id="code"></span><span id="CODE"></span>Code
</dt> <dd>

``` syntax
ARC_STATUS HalpCopyNVRamBuffer (
IN PCHAR NvDestPtr,
IN PCHAR NvSrcPtr,
IN ULONG Length )
{

ULONG PageSelect1, ByteSelect1;

ByteSelect1 = (NvDestPtr - (PUCHAR)HalpCMOSRamBase) & CONFIG_RAM_BYTE_MASK;

ByteSelect1 = (NvDestPtr - (PUCHAR)HalpCMOSRamBase) & CONFIG_RAM_BYTE_MASK;
```

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

This warning is generated because the calculation is using 64-bit values, in this case pointers, and placing the result in a 32-bit **ULONG**.

</dd> <dt>

<span id="Solution"></span><span id="solution"></span><span id="SOLUTION"></span>Solution
</dt> <dd>

Type cast the result of the calculation to a **ULONG** as shown here:

`ByteSelect1 = (ULONG)(NvDestPtr - (PUCHAR)HalpCMOSRamBase) & CONFIG_RAM_BYTE_MASK;`

Typecasting the result lets the compiler know you are sure about the result. That being said, make certain you understand the calculation and really are sure it will fit in a 32-bit **ULONG**.

If the result may not fit in a 32-bit **ULONG**, change the base type of the variable that will hold the result.

</dd> </dl>

## Warning C4311 - Example 1

'type cast' : pointer truncation from 'void \*\_\_ptr64 ' to 'unsigned long '

<dl> <dt>

<span id="Code"></span><span id="code"></span><span id="CODE"></span>Code
</dt> <dd>

``` syntax
ULONG HalpMapDebugPort(
IN ULONG ComPort,
OUT PULONG ReadQva,
OUT PULONG WriteQva)
{
ULONG ComPortAddress;

ULONG PortQva;

// Compute the port address, based on the desired com port.

switch( ComPort ){
case 1:
   ComPortAddress = COM1_ISA_PORT_ADDRESS;
   break;

case 2:
default:
   ComPortAddress = COM2_ISA_PORT_ADDRESS;
}
PortQva = (ULONG)HAL_MAKE_QVA(CIA_PCI_SPARSE_IO_PHYSICAL) + ComPortAddress;

// Return the QVAs for read and write access.

*ReadQva = PortQva;
*WriteQva = PortQva;

return ComPortAddress;
}
```

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

This entire function deals with addresses as integers, necessitating the need to type those integers in a portable way. All the local variables, intermediate values in calculations, and return values should be portable types.

</dd> <dt>

<span id="Solution"></span><span id="solution"></span><span id="SOLUTION"></span>Solution
</dt> <dd>

``` syntax
ULONG_PTR HalpMapDebugPort(
IN ULONG ComPort,
OUT PULONG_PTR ReadQva,
OUT PULONG_PTR WriteQva)
{
ULONG_PTR ComPortAddress;

ULONG_PTR PortQva;

// Compute the port address, based on the desired com port.

switch( ComPort ){
case 1:
   ComPortAddress = COM1_ISA_PORT_ADDRESS;
   break;

case 2:
default:
   ComPortAddress = COM2_ISA_PORT_ADDRESS;
}

PortQva = (ULONG_PTR)HAL_MAKE_QVA(CIA_PCI_SPARSE_IO_PHYSICAL) + ComPortAddress;

// Return the QVAs for read and write access.

*ReadQva = PortQva;
*WriteQva = PortQva;

return ComPortAddress;
}
```

**PULONG\_PTR** is a pointer that is itself 32 bits for 32-bit Windows and 64 bits for 64-bit Windows. It points to an unsigned integer, **ULONG\_PTR**, that is 32 bits for 32-bit Windows and 64 bits for 64-bit Windows.

</dd> </dl>

## Warning C4311 - Example 2

'type cast' : pointer truncation from 'void \*\_\_ptr64 ' to 'unsigned long '

<dl> <dt>

<span id="Code"></span><span id="code"></span><span id="CODE"></span>Code
</dt> <dd>

``` syntax
BOOLEAN
HalpMapIoSpace (
VOID
)
{
PVOID PciIoSpaceBase;
PciIoSpaceBase = HAL_MAKE_QVA( CIA_PCI_SPARSE_IO_PHYSICAL );

//Map base addresses in QVA space.

HalpCMOSRamBase = (PVOID)((ULONG)PciIoSpaceBase + CMOS_ISA_PORT_ADDRESS);
```

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

Even though all QVA (Quasi Virtual Address) values are really 32-bit values at this stage and will fit in a **ULONG**, it is more consistent to treat all addresses as **ULONG\_PTR** values when possible.

The pointer PciIoSpaceBase holds the QVA that is created in the macro HAL\_MAKE\_QVA. This macro returns a 64-bit value with the top 32 bits set to zero so the math will work. We could simply leave the code to truncate the pointer into a **ULONG**, but this practice is discouraged to enhance code maintainability and portability. For example, the contents of a QVA might change in the future to use some of the upper bits at this level, breaking the code.

</dd> <dt>

<span id="Solution"></span><span id="solution"></span><span id="SOLUTION"></span>Solution
</dt> <dd>

Be safe and use **ULONG\_PTR** for all address and pointer math.

`HalpCMOSRamBase = (PVOID)((ULONG_PTR)PciIoSpaceBase + CMOS_ISA_PORT_ADDRESS);`

</dd> </dl>

## Warning C4311 Example 3

'type cast' : pointer truncation from 'void \*\_\_ptr64 ' to 'unsigned long '

<dl> <dt>

<span id="Code"></span><span id="code"></span><span id="CODE"></span>Code
</dt> <dd>

``` syntax
PVOID
HalDereferenceQva(
PVOID Qva,
INTERFACE_TYPE InterfaceType,
ULONG BusNumber)

if ( ((ULONG) Qva & QVA_SELECTORS) == QVA_ENABLE ) {

return( (PVOID)( (ULONG)Qva << IO_BIT_SHIFT ) );
} 
else {
return (Qva);
}
```

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

The compiler warns about the address of (&) and left shift (<<) operators if they are applied to pointer types. In the above code, Qva is a **PVOID** value. We need to cast that to an integer type to perform the math. Because the code must be portable, use **ULONG\_PTR** instead of **ULONG**.

</dd> <dt>

<span id="Solution"></span><span id="solution"></span><span id="SOLUTION"></span>Solution
</dt> <dd>

``` syntax
if ( ((ULONG_PTR) Qva & QVA_SELECTORS) == QVA_ENABLE ) {
  return( (PVOID)( (ULONG_PTR)Qva << IO_BIT_SHIFT ) );
```

</dd> </dl>

## Warning C4311 Example 4

'type cast' : pointer truncation from 'void \*\_\_ptr64 ' to 'unsigned long '

<dl> <dt>

<span id="Code"></span><span id="code"></span><span id="CODE"></span>Code
</dt> <dd>

``` syntax
TranslatedAddress->LowPart = (ULONG)HalCreateQva(
*TranslatedAddress, va);
```

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

TranslatedAddress is a union that looks something like the following:

``` syntax
typedef union
   Struct {
      ULONG LowPart;
      LONG Highpart;
   }
   LONGLONG QuadPart;
}
```

</dd> <dt>

<span id="Solution"></span><span id="solution"></span><span id="SOLUTION"></span>Solution
</dt> <dd>

Knowing what the rest of the code might place in Highpart, we can select either of the solutions shown here.

`TranslatedAddress->LowPart = PtrToUlong(HalCreateQva(*TranslatedAddress,va) );`

The **PtrToUlong** macro truncates the pointer returned by **HalCreateQva** to 32 bits. We know that the QVA returned by **HalCreateQva** has the upper 32 bits set to zero and the very next line of code sets TranslatedAddress->Highpart to zero.

With caution, we could use the following:

`TranslatedAddress->QuadPart = (LONGLONG)HalCreateQva(*TranslatedAddress,va);`

This works in this example: the **HalCreateQva** macro is returning 64 bits, with the upper 32 bits set to zero. Just be careful not to leave the upper 32 bits undefined in a 32-bit environment, which this second solution may actually do.

</dd> </dl>

## Warning C4311 Example 5

'type cast' : pointer truncation from 'void \*\_\_ptr64 ' to 'unsigned long '

<dl> <dt>

<span id="Code"></span><span id="code"></span><span id="CODE"></span>Code
</dt> <dd>

``` syntax
VOID
HalpCiaProgramDmaWindow(
PWINDOW_CONTROL_REGISTERS WindowRegisters,
PVOID MapRegisterBase
)
{
CIA_WBASE Wbase;

Wbase.all = 0;
Wbase.Wen = 1;
Wbase.SgEn = 1;
Wbase.Wbase = (ULONG)(WindowRegisters->WindowBase) >> 20;
```

</dd> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description
</dt> <dd>

WindowRegisters->WindowBase is a pointer and is now 64 bits. The code says to right-shift this value 20 bits. The compiler will not let us use the right-shift (>>) operator on a pointer; therefore, we need to cast it to some sort of integer.

</dd> <dt>

<span id="Solution"></span><span id="solution"></span><span id="SOLUTION"></span>Solution
</dt> <dd>

`Wbase.Wbase= PtrToUlong ( (PVOID) ((ULONG_PTR) (WindowRegisters->WindowBase) >> 20));`

Casting to a **ULONG\_PTR** is just what we need. The next problem is Wbase. Wbase is a **ULONG** and is 32 bits. In this case, we know that the 64-bit pointer WindowRegisters->WindowBase is valid in the lower 32 bits even after being shifted. This makes use of the **PtrToUlong** macro acceptable, because it will truncate the 64-bit pointer into a 32-bit **ULONG**. The **PVOID** cast is necessary because **PtrToUlong** expects a pointer argument. When you look at the resulting assembler code, all this C code casting becomes just a load quad, shift right, and store long.

</dd> </dl>

 

 





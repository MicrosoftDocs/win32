---
Description: 'The SIMULATE\_CAPS\_1 structure contains information about the types of simulations a spooler supports.'
ms.assetid: '17f5d8bf-a3e7-4ff5-9019-24c66875b786'
title: 'SIMULATE\_CAPS\_1 structure'
---

# SIMULATE\_CAPS\_1 structure

The SIMULATE\_CAPS\_1 structure contains information about the types of simulations a spooler supports.

## Syntax


```C++
typedef struct _SIMULATE_CAPS_1 {
  DWORD dwLevel;
  DWORD dwPageOrderFlags;
  DWORD dwNumberOfCopies;
  DWORD dwCollate;
  DWORD dwNupOptions;
} SIMULATE_CAPS_1, *PSIMULATE_CAPS_1;
```



## Members

<dl> <dt>

**dwLevel**
</dt> <dd>

Specifies the version of this structure. This value must be 1.

</dd> <dt>

**dwPageOrderFlags**
</dt> <dd>

Specifies the order in which pages will be printed. This member can be set to one of the following values:



| Flag                      | Definition                                                                                                                                                                                                                                                                |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BOOKLET\_PRINT<br/> | Pages should be printed in booklet form, with two document pages printed on one side of a physical page. In landscape mode, the two document pages are printed side-by-side on the paper. In portrait mode, the two document pages are printed top-and-bottom.<br/> |
| NORMAL\_PRINT<br/>  | Pages should be printed in normal order: page 1, page 2, and so on.<br/>                                                                                                                                                                                            |
| REVERSE\_PRINT<br/> | Pages should be printed in reverse order: last page, next-to-last page, and so on.<br/>                                                                                                                                                                             |



 

</dd> <dt>

**dwNumberOfCopies**
</dt> <dd>

Specifies the maximum number of copies the spooler can handle.

</dd> <dt>

**dwCollate**
</dt> <dd>

Specifies whether the spooler supports collation. A value of 1 indicates that the spooler supports collation, and a value of 0 indicates that it does not.

</dd> <dt>

**dwNupOptions**
</dt> <dd>

Is a bitmask representing the various numbers of document pages the printer can print on a physical page. The least significant bit represents 1 document page per page, the next bit represents 2 document pages per page, the next bit represents 3 document pages per physical page, and so on. For example, 0x0000810B indicates that the spooler supports 1, 2, 4, 9, and 16 document pages per physical page.

</dd> </dl>

## Remarks

The **IPrintCoreUI2::QuerySimulationSupport** method uses this structure to report the spooler's level of simulation support to a user-interface plug-in.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Printoem.h (include Printoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreUI2::QuerySimulationSupport**](iprintcoreui2-querysimulationsupport.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20SIMULATE_CAPS_1%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






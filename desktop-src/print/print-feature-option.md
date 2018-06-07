---
Description: The PRINT\_FEATURE\_OPTION structure contains information about a feature-option pair, where the option is one option of a particular feature.
ms.assetid: 82c9c54b-f124-46d7-a3c9-a17fd8028412
title: PRINT\_FEATURE\_OPTION structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# PRINT\_FEATURE\_OPTION structure

The PRINT\_FEATURE\_OPTION structure contains information about a feature-option pair, where the option is one option of a particular feature.

## Syntax


```C++
typedef struct _PRINT_FEATURE_OPTION {
  PCSTR pszFeature;
  PCSTR pszOption;
} PRINT_FEATURE_OPTION;
```



## Members

<dl> <dt>

**pszFeature**
</dt> <dd>

The printing feature.

</dd> <dt>

**pszOption**
</dt> <dd>

One of the options for the printing feature.

</dd> </dl>

## Remarks

This structure is used by methods that belong to the **IPrintCoreHelper**, **IPrintCoreHelperPS**, and **IPrintCoreHelperUni** interfaces. The methods are listed in the See Also section.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Prcomoem.h (include Prcomoem.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreHelper::SetOptions**](iprintcorehelper-setoptions.md)
</dt> <dt>

[**IPrintCoreHelper::WhyConstrained**](iprintcorehelper-whyconstrained.md)
</dt> <dt>

[**IPrintCoreHelperPS::SetOptions**](iprintcorehelperps-setoptions.md)
</dt> <dt>

[**IPrintCoreHelperPS::WhyConstrained**](iprintcorehelperps-whyconstrained.md)
</dt> <dt>

[**IPrintCoreHelperUni::SetOptions**](iprintcorehelperuni-setoptions.md)
</dt> <dt>

[**IPrintCoreHelperUni::WhyConstrained**](iprintcorehelperuni-whyconstrained.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20PRINT_FEATURE_OPTION%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






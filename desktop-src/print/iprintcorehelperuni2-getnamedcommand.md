---
Description: 'The GetNamedCommand method returns the specified command.'
ms.assetid: 'A9C9C69E-8C89-4131-996F-A48AD9E9D244'
title: 'IPrintCoreHelperUni2::GetNamedCommand method'
---

# IPrintCoreHelperUni2::GetNamedCommand method

The **GetNamedCommand** method returns the specified command.

## Syntax


```C++
HRESULT GetNamedCommand(
  [in]  PDEVMODE pDevmode,
  [in]  DWORD    cbSize,
  [in]  LPCWSTR  pszCommandName,
  [out] PBYTE    **ppCommandBytes,
  [out] DWORD    *pcbCommandSize
);
```



## Parameters

<dl> <dt>

*pDevmode* \[in\]
</dt> <dd>

A pointer to a DEVMODE structure.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

The number of bytes in *pDevmode*, not the number of bytes written.

</dd> <dt>

*pszCommandName* \[in\]
</dt> <dd>

The command name. This parameter accepts standard command names from the GPD, except for those that require an \*Order attribute. Those six sections of ordered command sequences are accessible via the following special command names:

-   L"SectionJobSetup"
-   L"SectionDocSetup"
-   L"SectionPageSetup"
-   L"SectionPageFinish"
-   L"SectionDocFinish"
-   L"SectionJobFinish"

</dd> <dt>

*ppCommandBytes* \[out\]
</dt> <dd>

The output buffer. This buffer does not need to be freed by the caller.

</dd> <dt>

*pcbCommandSize* \[out\]
</dt> <dd>

The size of the output buffer.

</dd> </dl>

## Return value

This method returns an **HRESULT** value.

## Remarks

The **GetNamedCommand** method will not return commands containing references to Standard Variables.

## Requirements



|                            |                                                                                       |
|----------------------------|---------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>    |
| Header<br/>          | <dl> <dt>Prcomoem.h</dt> </dl> |



## See also

<dl> <dt>

[**IPrintCoreHelperUni2**](iprintcorehelperuni2-interface.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreHelperUni2::GetNamedCommand%20method%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")






---
title: VERSIONINFO resource
description: Defines a version-information resource. The resource contains such information about the file as its version number, its intended operating system, and its original filename. The resource is intended to be used with the Version Information functions.
ms.assetid: be4fbf3d-ca30-4de1-b17a-691a316edfad
keywords:
- VERSIONINFO resource Menus and Other Resources
topic_type:
- apiref
api_name:
- VERSIONINFO
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# VERSIONINFO resource

Defines a version-information resource. The resource contains such information about the file as its version number, its intended operating system, and its original filename. The resource is intended to be used with the [Version Information](./version-information.md) functions.

There are two ways to format a **VERSIONINFO** statement:

``` syntax
versionID VERSIONINFO fixed-info  { block-statement . . . }
```

\- or -

``` syntax
versionID VERSIONINFO 
fixed-info
BEGIN
block-statement
. . .
END
```

## Parameters

<dl> <dt>

<span id="versionID"></span><span id="versionid"></span><span id="VERSIONID"></span>*versionID*
</dt> <dd>

Version-information resource identifier. This value must be 1.

</dd> <dt>

<span id="fixed-info"></span><span id="FIXED-INFO"></span>*fixed-info*
</dt> <dd>

Version information, such as the file version and the intended operating system. This parameter consists of the following statements.



| Statement                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **FILEVERSION** *version*         | Binary version number for the file. The *version* consists of two 32-bit integers, defined by four 16-bit integers. For example, "FILEVERSION 3,10,0,61" is translated into two doublewords: 0x0003000a and 0x0000003d, in that order. Therefore, if *version* is defined by the **DWORD** values *dw1* and *dw2*, they need to appear in the **FILEVERSION** statement as follows: `HIWORD(dw1)`, `LOWORD(dw1)`, `HIWORD(dw2)`, `LOWORD(dw2)`. |
| **PRODUCTVERSION** *version*      | Binary version number for the product with which the file is distributed. The *version* parameter is two 32-bit integers, defined by four 16-bit integers. For more information about *version*, see the **FILEVERSION** description.                                                                                                                                                                                                           |
| **FILEFLAGSMASK** *fileflagsmask* | Indicates which bits in the **FILEFLAGS** statement are valid. For 16-bit Windows, this value is 0x3f.                                                                                                                                                                                                                                                                                                                                          |
| **FILEFLAGS** *fileflags*         | Attributes of the file.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **FILEOS** *fileos*               | Operating system for which this file was designed. The *fileos* parameter can be one of the operating system values given in the Remarks section.                                                                                                                                                                                                                                                                                               |
| **FILETYPE** *filetype*           | General type of file. The *filetype* parameter can be one of the file type values listed in the Remarks section.                                                                                                                                                                                                                                                                                                                                |
| **FILESUBTYPE** *subtype*         | Function of the file. The *subtype* parameter is zero unless the *filetype* parameter in the **FILETYPE** statement is VFT\_DRV, VFT\_FONT, or VFT\_VXD. For a list of file subtype values, see the Remarks section.                                                                                                                                                                                                                            |



 

</dd> <dt>

<span id="block-statement"></span><span id="BLOCK-STATEMENT"></span>*block-statement*
</dt> <dd>

Specifies one or more version-information blocks. A block can contain string information or variable information. For more information, see [**StringFileInfo Block**](stringfileinfo-block.md) or [**VarFileInfo Block**](varfileinfo-block.md).

</dd> </dl>

## Remarks

To use the constants specified with the **VERSIONINFO** statement, you must include the Winver.h or Windows.h header file in the resource-definition file.

The following list describes the parameters used in the **VERSIONINFO** statement:

<dl> <dt>

<span id="fileflags"></span><span id="FILEFLAGS"></span>*fileflags*
</dt> <dd>

A combination of the following values.



| Value                      | Description                                                                                                                                                                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **VS\_FF\_DEBUG**          | File contains debugging information or is compiled with debugging features enabled.                                                                                                                                                                                         |
| **VS\_FF\_PATCHED**        | File has been modified and is not identical to the original shipping file of the same version number.                                                                                                                                                                       |
| **VS\_FF\_PRERELEASE**     | File is a development version, not a commercially released product.                                                                                                                                                                                                         |
| **VS\_FF\_PRIVATEBUILD**   | File was not built using standard release procedures. If this value is given, the [**StringFileInfo block**](stringfileinfo-block.md) must contain a **PrivateBuild** string.                                                                                              |
| **VS\_FF\_SPECIALBUILD**   | File was built by the original company using standard release procedures but is a variation of the standard file of the same version number. If this value is given, the [**StringFileInfo** block](stringfileinfo-block.md) block must contain a **SpecialBuild** string. |
| **VS\_FFI\_FILEFLAGSMASK** | A combination of all the preceding values.                                                                                                                                                                                                                                  |



 

</dd> <dt>

<span id="fileos"></span><span id="FILEOS"></span>*fileos*
</dt> <dd>

One of the following values.



| Value                   | Description                                                      |
|-------------------------|------------------------------------------------------------------|
| **VOS\_UNKNOWN**        | The operating system for which the file was designed is unknown. |
| **VOS\_DOS**            | File was designed for MS-DOS.                                    |
| **VOS\_NT**             | File was designed for 32-bit Windows.                            |
| **VOS\_\_WINDOWS16**    | File was designed for 16-bit Windows.                            |
| **VOS\_\_WINDOWS32**    | File was designed for 32-bit Windows.                            |
| **VOS\_DOS\_WINDOWS16** | File was designed for 16-bit Windows running with MS-DOS.        |
| **VOS\_DOS\_WINDOWS32** | File was designed for 32-bit Windows running with MS-DOS.        |
| **VOS\_NT\_WINDOWS32**  | File was designed for 32-bit Windows.                            |



 

The values 0x00002L, 0x00003L, 0x20000L and 0x30000L are reserved.

</dd> <dt>

<span id="filetype"></span><span id="FILETYPE"></span>*filetype*
</dt> <dd>

One of the following values.



| Value                | Description                                                                                                                 |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **VFT\_UNKNOWN**     | File type is unknown.                                                                                                       |
| **VFT\_APP**         | File contains an application.                                                                                               |
| **VFT\_DLL**         | File contains a dynamic-link library (DLL).                                                                                 |
| **VFT\_DRV**         | File contains a device driver. If *filetype* is **VFT\_DRV**, *subtype* contains a more specific description of the driver. |
| **VFT\_FONT**        | File contains a font. If *filetype* is VFT\_FONT, *subtype* contains a more specific description of the font.               |
| **VFT\_VXD**         | File contains a virtual device.                                                                                             |
| **VFT\_STATIC\_LIB** | File contains a static-link library.                                                                                        |



 

All other values are reserved for use by Microsoft.

</dd> <dt>

<span id="subtype"></span><span id="SUBTYPE"></span>*subtype*
</dt> <dd>

Additional information about the file type.

If *filetype* specifies **VFT\_DRV**, this parameter can be one of the following values.



| Value                             | Description                               |
|-----------------------------------|-------------------------------------------|
| **VFT2\_UNKNOWN**                 | Driver type is unknown.                   |
| **VFT2\_DRV\_COMM**               | File contains a communications driver.    |
| **VFT2\_DRV\_PRINTER**            | File contains a printer driver.           |
| **VFT2\_DRV\_KEYBOARD**           | File contains a keyboard driver.          |
| **VFT2\_DRV\_LANGUAGE**           | File contains a language driver.          |
| **VFT2\_DRV\_DISPLAY**            | File contains a display driver.           |
| **VFT2\_DRV\_MOUSE**              | File contains a mouse driver.             |
| **VFT2\_DRV\_NETWORK**            | File contains a network driver.           |
| **VFT2\_DRV\_SYSTEM**             | File contains a system driver.            |
| **VFT2\_DRV\_INSTALLABLE**        | File contains an installable driver.      |
| **VFT2\_DRV\_SOUND**              | File contains a sound driver.             |
| **VFT2\_DRV\_VERSIONED\_PRINTER** | File contains a versioned printer driver. |



 

If *filetype* specifies **VFT\_FONT**, this parameter can be one of the following values.



| Value                    | Description                    |
|--------------------------|--------------------------------|
| **VFT2\_UNKNOWN**        | Font type is unknown.          |
| **VFT2\_FONT\_RASTER**   | File contains a raster font.   |
| **VFT2\_FONT\_VECTOR**   | File contains a vector font.   |
| **VFT2\_FONT\_TRUETYPE** | File contains a TrueType font. |



 

If *filetype* specifies VFT\_VXD, this parameter must be the virtual-device identifier included in the virtual-device control block.

All *subtype* values not listed here are reserved for use by Microsoft.

</dd> <dt>

<span id="langID"></span><span id="langid"></span><span id="LANGID"></span>*langID*
</dt> <dd>

One of the following language codes.



| Code   | Language            | Code   | Language                  |
|--------|---------------------|--------|---------------------------|
| 0x0401 | Arabic              | 0x0415 | Polish                    |
| 0x0402 | Bulgarian           | 0x0416 | Portuguese (Brazil)       |
| 0x0403 | Catalan             | 0x0417 | Rhaeto-Romanic            |
| 0x0404 | Traditional Chinese | 0x0418 | Romanian                  |
| 0x0405 | Czech               | 0x0419 | Russian                   |
| 0x0406 | Danish              | 0x041A | Croato-Serbian (Latin)    |
| 0x0407 | German              | 0x041B | Slovak                    |
| 0x0408 | Greek               | 0x041C | Albanian                  |
| 0x0409 | U.S. English        | 0x041D | Swedish                   |
| 0x040A | Castilian Spanish   | 0x041E | Thai                      |
| 0x040B | Finnish             | 0x041F | Turkish                   |
| 0x040C | French              | 0x0420 | Urdu                      |
| 0x040D | Hebrew              | 0x0421 | Bahasa                    |
| 0x040E | Hungarian           | 0x0804 | Simplified Chinese        |
| 0x040F | Icelandic           | 0x0807 | Swiss German              |
| 0x0410 | Italian             | 0x0809 | U.K. English              |
| 0x0411 | Japanese            | 0x080A | Spanish (Mexico)          |
| 0x0412 | Korean              | 0x080C | Belgian French            |
| 0x0413 | Dutch               | 0x0C0C | Canadian French           |
| 0x0414 | Norwegian ? Bokmal  | 0x100C | Swiss French              |
| 0x0810 | Swiss Italian       | 0x0816 | Portuguese (Portugal)     |
| 0x0813 | Belgian Dutch       | 0x081A | Serbo-Croatian (Cyrillic) |
| 0x0814 | Norwegian ? Nynorsk |        |                           |



 

</dd> <dt>

<span id="charsetID"></span><span id="charsetid"></span><span id="CHARSETID"></span>*charsetID*
</dt> <dd>

One of the following character-set identifiers.



| Decimal | Hexadecimal | Character Set              |
|---------|-------------|----------------------------|
| 0       | 0000        | 7-bit ASCII                |
| 932     | 03A4        | Japan (Shift ? JIS X-0208) |
| 949     | 03B5        | Korea (Shift ? KSC 5601)   |
| 950     | 03B6        | Taiwan (Big5)              |
| 1200    | 04B0        | Unicode                    |
| 1250    | 04E2        | Latin-2 (Eastern European) |
| 1251    | 04E3        | Cyrillic                   |
| 1252    | 04E4        | Multilingual               |
| 1253    | 04E5        | Greek                      |
| 1254    | 04E6        | Turkish                    |
| 1255    | 04E7        | Hebrew                     |
| 1256    | 04E8        | Arabic                     |



 

</dd> <dt>

<span id="string-name"></span><span id="STRING-NAME"></span>*string-name*
</dt> <dd>

One of the following predefined names.



| Name                 | Description                                                                                                                                                                                                                                                                                                 |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Comments**         | Additional information that should be displayed for diagnostic purposes.                                                                                                                                                                                                                                    |
| **CompanyName**      | Company that produced the file—for example, `Microsoft Corporation` or `Standard Microsystems Corporation, Inc.` This string is required.                                                                                                                                                                   |
| **FileDescription**  | File description to be presented to users. This string may be displayed in a list box when the user is choosing files to install—for example, `Keyboard Driver for AT-Style Keyboards`. This string is required.                                                                                            |
| **FileVersion**      | Version number of the file—for example, `3.10` or `5.00.RC2`. This string is required.                                                                                                                                                                                                                      |
| **InternalName**     | Internal name of the file, if one exists—for example, a module name if the file is a dynamic-link library. If the file has no internal name, this string should be the original filename, without extension. This string is required.                                                                       |
| **LegalCopyright**   | Copyright notices that apply to the file. This should include the full text of all notices, legal symbols, copyright dates, and so on. This string is optional.                                                                                                                                             |
| **LegalTrademarks**  | Trademarks and registered trademarks that apply to the file. This should include the full text of all notices, legal symbols, trademark numbers, and so on. This string is optional.                                                                                                                        |
| **OriginalFilename** | Original name of the file, not including a path. This information enables an application to determine whether a file has been renamed by a user. The format of the name depends on the file system for which the file was created. This string is required.                                                 |
| **PrivateBuild**     | Information about a private version of the file—for example, `Built by TESTER1 on \\TESTBED`. This string should be present only if **VS\_FF\_PRIVATEBUILD** is specified in the *fileflags* parameter of the root block.                                                                                   |
| **ProductName**      | Name of the product with which the file is distributed. This string is required.                                                                                                                                                                                                                            |
| **ProductVersion**   | Version of the product with which the file is distributed—for example, `3.10` or `5.00.RC2`. This string is required.                                                                                                                                                                                       |
| **SpecialBuild**     | Text that specifies how this version of the file differs from the standard version—for example, `Private build for TESTER1 solving mouse problems on M250 and M250E computers`. This string should be present only if **VS\_FF\_SPECIALBUILD** is specified in the *fileflags* parameter of the root block. |



 

</dd> </dl>

Certain attributes are also supported for backward compatibility. For more information, see [Common Resource Attributes](common-resource-attributes.md).

## Examples

The following example defines a **VERSIONINFO** resource:

```c
#define VER_FILEVERSION             3,10,349,0
#define VER_FILEVERSION_STR         "3.10.349.0\0"

#define VER_PRODUCTVERSION          3,10,0,0
#define VER_PRODUCTVERSION_STR      "3.10\0"

#ifndef DEBUG
#define VER_DEBUG                   0
#else
#define VER_DEBUG                   VS_FF_DEBUG
#endif

VS_VERSION_INFO VERSIONINFO
FILEVERSION     VER_FILEVERSION
PRODUCTVERSION  VER_PRODUCTVERSION
FILEFLAGSMASK   VS_FFI_FILEFLAGSMASK
FILEFLAGS       (VER_PRIVATEBUILD|VER_PRERELEASE|VER_DEBUG)
FILEOS          VOS__WINDOWS32
FILETYPE        VFT_DLL
FILESUBTYPE     VFT2_UNKNOWN
BEGIN
    BLOCK "StringFileInfo"
    BEGIN
        BLOCK "040904E4"
        BEGIN
            VALUE "CompanyName",      VER_COMPANYNAME_STR
            VALUE "FileDescription",  VER_FILEDESCRIPTION_STR
            VALUE "FileVersion",      VER_FILEVERSION_STR
            VALUE "InternalName",     VER_INTERNALNAME_STR
            VALUE "LegalCopyright",   VER_LEGALCOPYRIGHT_STR
            VALUE "LegalTrademarks1", VER_LEGALTRADEMARKS1_STR
            VALUE "LegalTrademarks2", VER_LEGALTRADEMARKS2_STR
            VALUE "OriginalFilename", VER_ORIGINALFILENAME_STR
            VALUE "ProductName",      VER_PRODUCTNAME_STR
            VALUE "ProductVersion",   VER_PRODUCTVERSION_STR
        END
    END

    BLOCK "VarFileInfo"
    BEGIN
        /* The following line should only be modified for localized versions.     */
        /* It consists of any number of WORD,WORD pairs, with each pair           */
        /* describing a language,codepage combination supported by the file.      */
        /*                                                                        */
        /* For example, a file might have values "0x409,1252" indicating that it  */
        /* supports English language (0x409) in the Windows ANSI codepage (1252). */

        VALUE "Translation", 0x409, 1252

    END
END
```

## See also

<dl> <dt>

[Using Version Information](./using-version-information.md)
</dt> <dt>

[Version Information](./version-information.md)
</dt> </dl>

 

 

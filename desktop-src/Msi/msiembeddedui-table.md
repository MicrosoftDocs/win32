---
description: The MsiEmbeddedUI table defines a user interface embedded in the Windows Installer package.
ms.assetid: d4176f99-e819-4b5a-bd06-1a2965891f9a
title: MsiEmbeddedUI Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiEmbeddedUI Table

The MsiEmbeddedUI table defines a user interface embedded in the Windows Installer package.

**[Windows Installer 4.0 or earlier](not-supported-in-windows-installer-4-0.md):** Not supported. This table is available beginning with Windows Installer 4.5.

The MsiEmbeddedUI table has the following columns.



| Column        | Type                               | Key | Nullable |
|---------------|------------------------------------|-----|----------|
| MsiEmbeddedUI | [Identifier](identifier.md)       | Y   | N        |
| FileName      | [Text](text.md)                   | N   | N        |
| Attributes    | [Integer](integer.md)             | N   | N        |
| MessageFilter | [DoubleInteger](doubleinteger.md) | N   | Y        |
| Data          | [Binary](binary.md)               | N   | N        |



 

## Columns

<dl> <dt>

<span id="MsiEmbeddedUI"></span><span id="msiembeddedui"></span><span id="MSIEMBEDDEDUI"></span>MsiEmbeddedUI
</dt> <dd>

The primary key for the table.

</dd> <dt>

<span id="FileName"></span><span id="filename"></span><span id="FILENAME"></span>FileName
</dt> <dd>

The name of the file that receives the binary information in the Data column. The name of the file is required to include an extension. For example, the name *embeddedui.dll* is acceptable, but *embeddedui* is unacceptable. The name may be localized. This field can contain a short file name or a long file name, but it cannot contain both. The format of this field is like the [Filename](filename.md) column data type except that the vertical bar (\|) separator for the short file name/long file name syntax is not available. Because some web servers can be case sensitive, FileName should match the case of the source files exactly to ensure support of Internet downloads.

</dd> <dt>

<span id="Attributes"></span><span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes
</dt> <dd>

Information about the data in the Data column. The value in this field can contain one or more of the following constants.



| Constant                      | Hexadecimal | Decimal | Meaning                                                                                                                                                                                                                          |
|-------------------------------|-------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| None                          | 0x00        | 0       | The file is not the DLL file for the user interface. It may be a resource file used by the user interface.                                                                                                                       |
| **msidbEmbeddedUI**           | 0x01        | 1       | The primary DLL file for the user interface. No more than one row in the table can be marked with this attribute. If multiple rows are marked with this attribute, it is an error and it cannot be guaranteed which DLL is used. |
| **msidbEmbeddedHandlesBasic** | 0x02        | 2       | Enables the installer to invoke the embedded UI during a basic UI level installation. The installer ignores this attribute if it is not combined with the **msidbEmbeddedUI** attribute.                                         |



 

</dd> <dt>

<span id="MessageFilter"></span><span id="messagefilter"></span><span id="MESSAGEFILTER"></span>MessageFilter
</dt> <dd>

Specifies the types of messages that are sent to the user interface DLL. This column is only relevant for rows with the **msidbEmbeddedUI** attribute. This field should be null if a row references a resource file and the value of Attributes is null. If a row references a user interface DLL, the value in this column should not be null.

The value in this column can be a combination of the following values. The installer ignores any other values.



| Constant                           | Hexadecimal | Decimal   | Description                                                                                                  |
|------------------------------------|-------------|-----------|--------------------------------------------------------------------------------------------------------------|
| **INSTALLLOGMODE\_FATALEXIT**      | 0x00001     | 1         | Premature termination.                                                                                       |
| **INSTALLLOGMODE\_ERROR**          | 0x00002     | 2         | Error messages.                                                                                              |
| **INSTALLLOGMODE\_WARNING**        | 0x00004     | 4         | Warning messages.                                                                                            |
| **INSTALLLOGMODE\_USER**           | 0x00008     | 8         | User messages.                                                                                               |
| **INSTALLLOGMODE\_INFO**           | 0x00010     | 16        | Unlogged status messages.                                                                                    |
| **INSTALLLOGMODE\_FILESINUSE**     | 0x00020     | 32        | Files currently held in use.                                                                                 |
| **INSTALLLOGMODE\_RESOLVESOURCE**  | 0x00040     | 64        | Source resolution requests.                                                                                  |
| **INSTALLLOGMODE\_OUTOFDISKSPACE** | 0x00080     | 128       | Disk space messages.                                                                                         |
| **INSTALLLOGMODE\_ACTIONSTART**    | 0x00100     | 256       | Action start messages.                                                                                       |
| **INSTALLLOGMODE\_ACTIONDATA**     | 0x00200     | 512       | Action data messages.                                                                                        |
| **INSTALLLOGMODE\_PROGRESS**       | 0x00400     | 1024      | Progress messages.                                                                                           |
| **INSTALLLOGMODE\_COMMONDATA**     | 0x00800     | 2048      | UI initialization messages.                                                                                  |
| **INSTALLLOGMODE\_INITIALIZE**     | 0x01000     | 4096      | UI startup messages sent when a product installation is starting.                                            |
| **INSTALLLOGMODE\_TERMINATE**      | 0x02000     | 8192      | UI shutdown messages sent after a product installation has finished.                                         |
| **INSTALLLOGMODE\_SHOWDIALOG**     | 0x04000     | 16384     | Messages sent prior to the display of UI dialog.                                                             |
| **INSTALLLOGMODE\_RMFILESINUSE**   | 0x02000000  | 33554432  | Files currently held in use.                                                                                 |
| **INSTALLLOGMODE\_INSTALLSTART**   | 0x04000000  | 67108864  | Installation of product begins. The message contains the product's ProductName and ProductCode.              |
| **INSTALLLOGMODE\_INSTALLEND**     | 0x08000000  | 134217728 | Installation of product ends. The message contains the product's ProductName, ProductCode, and return value. |



 

</dd> <dt>

<span id="Data"></span><span id="data"></span><span id="DATA"></span>Data
</dt> <dd>

This column contains binary information. If the Attribute field is marked with the **msidbEmbeddedUI** attribute, the information in this field must be a DLL. If the Attribute field is not the **msidbEmbeddedUI** attribute, the information in this field can be a resource file in any format.

</dd> </dl>

## Remarks

To use an embedded user interface, the setup developer must author this functionality into the Windows Installer package. The MsiEmbeddedUI table defines the embedded user interface. The DLL for the embedded UI should export the *InitializeEmbeddedUI*, *EmbeddedUIHandler*, and *ShutdownEmbeddedUI* functions. Packages that do not support an embedded user interface can use the Windows Installer internal user interface.

To run [Debugging Tools for Windows](https://www.microsoft.com/?ref=go) on an embedded user interface, use the techniques described in [Debugging Custom Actions](debugging-custom-actions.md). Set the value of MsiBreak to MsiEmbeddedUI.

For an example of an embedded custom UI see [Using an Embedded UI](using-an-embedded-ui.md).

 

 




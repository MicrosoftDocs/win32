---
description: The Microsoft XPS Document Writer (MXDW) is a print-to-file driver that enables a Windows application to create XML Paper Specification (XPS) document files.
ms.assetid: cb431700-f10f-4c53-9944-d6769895595d
title: Microsoft XPS Document Writer (MXDW)
ms.topic: article
ms.date: 10/26/2021
ms.custom: seo-windows-dev
---

# Microsoft XPS Document Writer (MXDW)

The Microsoft XPS Document Writer (MXDW) is a print-to-file driver that enables a Windows application to create XML Paper Specification (XPS) document files on versions of Windows starting with Windows XP with Service Pack 2 (SP2). Using the MXDW makes it possible for a Windows application to save its content as an XPS document without changing any of the application's program code.

If you create an XPS file, but don't have an app to save or store the contents, you can use the Microsoft XPS Document Writer printer to save all content of the XPS file. Microsoft XPS Document Writer comes pre-installed on Windows 10 and Windows 11, just press `Ctrl` + `P` to print/save an XPS file.

> [!NOTE]
> To install or reinstall the XPS Document Writer, Press Windows key + `R`, Type: "control printers", select `Enter`, select `Add printer`, select `The printer what I want isn't listed`, select `Add a local printer or network printer with manual settings`, select `Use an existing port`, select `Next`, select `Microsoft` from the left column, select `microsoft xps document writer` from the right column, select `Next` and the Microsoft XPS Document Writer will download.

For more information about V4 print driver, see [Exploring the Driver Options in the Wizard](/windows-hardware/drivers/print/exploring-the-driver-options-in-the-wizard).

## When to Use

As a **user**, you would select the MXDW when you want to create an XPS document from a Windows application that does not have the option to save its content as an XPS document.

As an **application developer**, you would recommend the MXDW to users who want to create XPS documents when your application does not offer the option to save as an XPS document. For more information on the XML Paper Specification and XPS documents, see [XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf) and [XPS Specification and License Downloads](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf).

The MXDW is installed automatically on Windows Vista and later versions of Windows and can be downloaded and installed on Windows XP with SP2 and Windows Server 2003.

## How to Use

When installed, the MXDW appears as an available print queue in the Print dialog box presented by an application. When the MXDW is selected as the printer, the user is prompted for the file name to create as the XPS Document that captures the print output of the application.

Application developers can customize the output of MXDW using the [MXDW configuration settings](mxdw-configuration-settings.md).

:::image type="content" source="images/choosingmxdwinvista.gif" alt-text="An image of the print dialog box that shows the selection of the microsoft xps document writer (mxdw).":::

## Where does Microsoft XPS Document Writer save to

The MXDW printer saves files in the Documents folder: ` C:\Users\user-name\Documents`. (Remember to replace `user-name` with your original username.)

## Related topics

- [XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
- [XPS Specification and License Downloads](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
- [isXPS Conformance Tool](/previous-versions/dotnet/netframework-3.0/aa348104(v=vs.85))
- [MXDW configuration settings](mxdw-configuration-settings.md)

---
description: The Microsoft XPS Document Writer (MXDW) is a print-to-file driver that enables a Windows application to create XML Paper Specification (XPS) document files on versions of Windows starting with Windows XP with Service Pack 2 (SP2).
ms.assetid: cb431700-f10f-4c53-9944-d6769895595d
title: Microsoft XPS Document Writer (MXDW)
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft XPS Document Writer (MXDW)

The Microsoft XPS Document Writer (MXDW) is a print-to-file driver that enables a Windows application to create XML Paper Specification (XPS) document files on versions of Windows starting with Windows XP with Service Pack 2 (SP2). Using the MXDW makes it possible for a Windows application to save its content as an XPS document without changing any of the application's program code.

## When to Use

As a user, you would select the MXDW when you want to create an XPS document from a Windows application that does not have the option to save its content as an XPS document.

As an application developer, you would recommend the MXDW to users who want to create XPS documents when your application does not offer the option to save as an XPS document. For more information on the XML Paper Specification and XPS documents, see [XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf) and [XPS Specification and License Downloads](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf).

The MXDW is installed automatically on Windows Vista and later versions of Windows and can be downloaded and installed on Windows XP with SP2 and Windows Server 2003.

## Installation

On Windows Vista and later versions of Windows, the MXDW is installed automatically when the operating system is installed.

**Windows XP with SP2 and Windows Server 2003**: Download and install either .Net Framework 3.0 or the XPS Essential Pack from the [Microsoft Download Center](https://www.microsoft.com/downloads/en/default.aspx).

## How to Use

When installed, the MXDW appears as an available print queue in the Print dialog box presented by an application. When the MXDW is selected as the printer, the user is prompted for the file name to create as the XPS Document that captures the print output of the application.

The following image shows the MXDW being selected as the printer in the Windows Vista common print dialog box.

![an image of the print dialog box that shows the selection of the microsoft xps document writer (mxdw)](images/choosingmxdwinvista.gif)

Application developers can customize the output of MXDW using the [MXDW configuration settings](mxdw-configuration-settings.md).

## Related topics

<dl> <dt>

[XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> <dt>

[XPS Specification and License Downloads](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> <dt>

[isXPS Conformance Tool](/previous-versions/dotnet/netframework-3.0/aa348104(v=vs.85))
</dt> <dt>

[MXDW configuration settings](mxdw-configuration-settings.md)
</dt> </dl>

 

 

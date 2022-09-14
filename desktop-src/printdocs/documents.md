---
description: This section describes the document technologies that are supported by Microsoft Windows.
ms.assetid: '14ae2c97-8596-46db-a55c-ef706d2cd00b'
title: XPS Documents
ms.topic: article
ms.date: 05/31/2018
---

# XPS Documents

This section describes the document technologies that are supported by Microsoft Windows.

-   [Choosing a Document Technology](#choosing-a-document-technology)
-   [In This Section](#in-this-section)
-   [XPS Document Tools](#xps-document-tools)
-   [Related topics](#related-topics)


## Choosing a Document Technology

Microsoft provides several different document technologies to support a variety of document applications:

-   **XPS and OpenXPS**

    XPS and OpenXPS are supported in Windows 8 and later versions of Windows. See the preceding diagram to determine the correct usage scenario for XPS and OpenXPS. For more information about these document technologies, see [Open XML Paper Specification (OpenXPS)](https://www.ecma-international.org/publications/standards/Ecma-388.htm).

    In the case of using OpenXPS with Windows 8 and Windows Server 2012, support is only provided via the [XPS Document API](documents-xps.md)

    If you need to convert between Microsoft XPS (MSXPS) and OpenXPS, then Microsoft has provided a tool (XPSConverter.exe) that allows you to convert MSXPS-formatted documents to the OpenXPS format and vice versa. The tool is part of the Windows Driver Kit (WDK). To download the WDK, see [How to get the WDK](/windows-hardware/drivers/download-the-wdk).

    And for more information about OpenXPS and Windows 8, see [OpenXPS Support in Windows](/windows-hardware/drivers/print/driver-support-for-openxps).

-   **XPS Document API**

    The XPS Document API is a native Windows API that supports the XPS OM. The XPS Document API was introduced in Windows 7 and can be used in user-mode programs and XPSDrv printer drivers.

    For more information, see the XPS Document API, and [XPS Digital Signature API](xps-digital-signatures.md).

    \*The XPS Document API is also supported in Windows Vista with Service Pack 2 (SP2) with the Platform Update for Windows Vista and Windows Server 2008 with SP2 using the Platform Update for Windows Server 2008. For more information about the Platform Update for Windows Vista or the Platform Update for Windows Server 2008, see [Platform Update for Windows Vista](/windows/desktop/win7ip/platform-update-for-windows-vista-portal)

-   **.NET Framework**

    .NET Framework provides XPS document support to user-mode, managed-code programs.

    .NET Framework 3.0 is supported on Windows XP with Service Pack 2 (SP2) and later versions of Windows client operating systems, and on Windows Server 2003 with Service Pack 2 (SP2) and later versions of Windows server operating systems.

    .NET Framework 3.5 is supported on Windows XP versions of Windows client operating systems, and on Windows Server 2003 and later versions of Windows server operating systems.

    > [!Note]  
    > We recommend the use of .NET Framework for creating XPS documents in client applications only, not in server applications unless the application exits periodically, as it would if it were a client application.

     

    For more information about document support in .NET Framework, see [Windows Presentation Foundation Documents](/previous-versions/dotnet/netframework-3.0/ms749165(v=vs.85)).

> [!Note]  
> To work with XPS documents in a program, use either the native XPS Document API or the .NET Framework; simultaneous use of both in the same program is not supported.

 

## In This Section

This section describes the native Windows document technologies that are supported by Microsoft Windows.



| Document technology                                                                   | Description                                                                                                                                                                                                                                |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [XPS Document API](documents-xps.md)<br/>                   | Provides a trustworthy format for electronic paper.<br/> The XPS Document API that is described in this section gives programs and XPSDrv print drivers access to the content and metadata of an XPS document.<br/> |
| [XPS Digital Signature API](xps-digital-signatures.md)<br/> | Enables document signing, verification of the signer's identity, and indication of whether an XPS document has changed since it was signed.<br/>                                                                          |
| [XPS Documents Glossary](xpsapi-glossary.md)<br/>           | Definitions of terms used by the [XPS Document API](documents-xps.md) and the [XPS Digital Signature API](xps-digital-signatures.md).<br/>                                                                              |



 

## XPS Document Tools

The following tools are available to assist you with testing and troubleshooting of XPS document files.

-   [IsXPS](/previous-versions/aa348104(v=vs.110))

    Tests a file's conformity to the XML Paper Specification (XPS) and the Open Packaging Conventions (OPC) Specification.

-   [XpsAnalyzer](/windows-hardware/drivers/devtest/xpsanalyzer)

    A command-prompt tool that analyzes XPS document files for compatibility with the XPS 1.0 specification.

-   [PTConform](/previous-versions/dd327476(v=msdn.10))

    A tool that checks the validity of PrintTicket and PrintCapabilities documents.

## Related topics

<dl> <dt>

[XPS Print API](./printing-with-the-xpsprint-api.md)
</dt> <dt>

[Packaging](/previous-versions/windows/desktop/opc/packaging)
</dt> <dt>

[Printing](./printdocs-printing.md)
</dt> <dt>
  
[Print Sample Program](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Windows%208%20app%20samples/%5BC%2B%2B%5D-Windows%208%20app%20samples/C%2B%2B/Windows%208%20app%20samples/Print%20sample%20(Windows%208))
</dt> </dl>

 


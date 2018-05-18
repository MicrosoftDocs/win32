---
Description: 'This topic describes cover pages.'
ms.assetid: '37bbff77-08a8-486f-ac26-d7b69a936e05'
title: Cover Pages
---

# Cover Pages

A *cover page* is a cover page template file (.cov) and user-defined information that is rendered onto the template at transmission time.

The Fax Service Client API supports the printing of cover pages. The cover page can be a *personal cover page* stored in a file on the local computer, or it can be a *common cover page* stored on the fax server. If a cover page is required, the user must either supply the fully qualified path to a cover page file, or the relative path to a common cover page file.

Administrators typically store common cover page files in the following location.

\\\\SERVERNAME\\FAX$\\Coverpg

On a single computer system, common cover page files are stored in the following folder.

%SYSTEMDRIVE%\\Documents and Settings\\All Users\\Application Data\\Microsoft\\Windows NT\\MSFax\\Common Coverpages

Users can add personal cover page files using the fax control panel application. The files must be stored in the user's **My Documents** standard folder in the following location.

CSIDL\_PERSONAL\\Fax\\Personal Coverpages

Additionally, in the Microsoft Win32 environment, if the user specifies a common cover page file, you must set the **UseServerCoverPage** member of the [**FAX\_COVERPAGE\_INFO**](-mfax-fax-coverpage-info-str.md) structure to **TRUE**. In the Component Object Model (COM) implementation environment, you must set the [**FaxDoc.ServerCoverpage Property**](-mfax-ifaxdoc-get-servercoverpage-vb.md) equal to **TRUE**.

A fax client application can call the [**FaxPrintCoverPage**](-mfax-faxprintcoverpage.md) function to print a cover page to a fax printer device context. For more information, see [Printing a Fax to a Device Context](-mfax-printing-a-fax-to-a-device-context.md) and [Sending a Cover Page](-mfax-sending-a-cover-page.md). For more information about folders in the user profile, see [SHGetSpecialFolderLocation](http://msdn.microsoft.com/library/en-us/shellcc/platform/shell/reference/functions/shgetspecialfolderlocation.asp).

 

 




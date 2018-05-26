---
Description: The ICertView interface is used by properly authorized clients to view the Certificate Services database.
ms.assetid: c8f316dd-186b-4e4a-b0ce-561a23b266cb
title: Viewing the Certificate Services Database
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Viewing the Certificate Services Database

The [**ICertView**](/windows/win32/Certview/nn-certview-icertview?branch=master) interface is used by properly authorized clients to view the Certificate Services database. It should be noted that, as part of the shipped product, the Certification Authority MMC snap-in can be used to view the Certificate Services database. [**ICertView**](/windows/win32/Certview/nn-certview-icertview?branch=master) is provided for programmatically viewing the database. Support for the **ICertView** interface begins with Windows XP.

A properly authorized client means a user who has been granted permission to view the Certificate Services database; the Certification Authority MMC snap-in can be used to grant or restrict access to view the database (under **Properties** for the [*certification authority*](security.c_gly#-security-certification-authority-gly), click the **Security** tab). Additionally, to use the [**ICertView**](/windows/win32/Certview/nn-certview-icertview?branch=master) object, the client workstation is required to have installed the Certificate Services client components.

Although there are various scenarios for using [**ICertView**](/windows/win32/Certview/nn-certview-icertview?branch=master) and its related interfaces, the following depicts one possible sequence for developing a client application based on **ICertView**:

**To view the Certificate Services database**

1.  After obtaining an instance of the [**ICertView**](/windows/win32/Certview/nn-certview-icertview?branch=master) object, call [**ICertView::OpenConnection**](/windows/win32/Certview/nf-certview-icertview-openconnection?branch=master) to communicate with a [*certification authority*](security.c_gly#-security-certification-authority-gly) on a specific computer.
2.  Call [**ICertView::SetResultColumnCount**](/windows/win32/Certview/nf-certview-icertview-setresultcolumncount?branch=master) to specify the number of columns in the view; this call is also used to specify a default view. If a default view is not specified in the call, the caller must call [**ICertView::SetResultColumn**](/windows/win32/Certview/nf-certview-icertview-setresultcolumn?branch=master) for each of the columns to be contained in the view.
3.  Optional. Specify sorting criteria and/or qualifying criteria for the database query by calling the [**ICertView::SetRestriction**](/windows/win32/Certview/nf-certview-icertview-setrestriction?branch=master) function. Qualifying criteria consists of informing the view to retrieve data based on qualifiers such as Greater Than, Less Than, Equal To, and so on.
4.  Call [**ICertView::OpenView**](/windows/win32/Certview/nf-certview-icertview-openview?branch=master) to retrieve the data in the view; the view's data will consist of the columns requested by means of [**ICertView::SetResultColumnCount**](/windows/win32/Certview/nf-certview-icertview-setresultcolumncount?branch=master) (and if a default view was not specified, [**ICertView::SetResultColumn**](/windows/win32/Certview/nf-certview-icertview-setresultcolumn?branch=master)). If [**ICertView::SetRestriction**](/windows/win32/Certview/nf-certview-icertview-setrestriction?branch=master) was called, data in the columns will be sorted and/or qualified. **ICertView::OpenView** creates a [**IEnumCERTVIEWROW**](/windows/win32/Certview/nn-certview-ienumcertviewrow?branch=master) object, which can be used to enumerate the view's rows.
5.  Use the [**IEnumCERTVIEWROW**](/windows/win32/Certview/nn-certview-ienumcertviewrow?branch=master) methods [**IEnumCERTVIEWROW::EnumCertViewAttribute**](/windows/win32/Certview/nf-certview-ienumcertviewrow-enumcertviewattribute?branch=master), [**IEnumCERTVIEWROW::EnumCertViewColumn**](/windows/win32/Certview/nf-certview-ienumcertviewrow-enumcertviewcolumn?branch=master), and [**IEnumCERTVIEWROW::EnumCertViewExtension**](/windows/win32/Certview/nf-certview-ienumcertviewrow-enumcertviewextension?branch=master) to retrieve attribute, column, and extension data as desired.

 

 




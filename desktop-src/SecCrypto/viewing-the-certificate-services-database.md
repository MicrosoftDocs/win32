---
description: The ICertView interface is used by properly authorized clients to view the Certificate Services database.
ms.assetid: c8f316dd-186b-4e4a-b0ce-561a23b266cb
title: Viewing the Certificate Services Database
ms.topic: article
ms.date: 05/31/2018
---

# Viewing the Certificate Services Database

The [**ICertView**](/windows/desktop/api/Certview/nn-certview-icertview) interface is used by properly authorized clients to view the Certificate Services database. It should be noted that, as part of the shipped product, the Certification Authority MMC snap-in can be used to view the Certificate Services database. [**ICertView**](/windows/desktop/api/Certview/nn-certview-icertview) is provided for programmatically viewing the database. Support for the **ICertView** interface begins with Windows XP.

A properly authorized client means a user who has been granted permission to view the Certificate Services database; the Certification Authority MMC snap-in can be used to grant or restrict access to view the database (under **Properties** for the [*certification authority*](../secgloss/c-gly.md), click the **Security** tab). Additionally, to use the [**ICertView**](/windows/desktop/api/Certview/nn-certview-icertview) object, the client workstation is required to have installed the Certificate Services client components.

Although there are various scenarios for using [**ICertView**](/windows/desktop/api/Certview/nn-certview-icertview) and its related interfaces, the following depicts one possible sequence for developing a client application based on **ICertView**:

**To view the Certificate Services database**

1.  After obtaining an instance of the [**ICertView**](/windows/desktop/api/Certview/nn-certview-icertview) object, call [**ICertView::OpenConnection**](/windows/desktop/api/Certview/nf-certview-icertview-openconnection) to communicate with a [*certification authority*](../secgloss/c-gly.md) on a specific computer.
2.  Call [**ICertView::SetResultColumnCount**](/windows/desktop/api/Certview/nf-certview-icertview-setresultcolumncount) to specify the number of columns in the view; this call is also used to specify a default view. If a default view is not specified in the call, the caller must call [**ICertView::SetResultColumn**](/windows/desktop/api/Certview/nf-certview-icertview-setresultcolumn) for each of the columns to be contained in the view.
3.  Optional. Specify sorting criteria and/or qualifying criteria for the database query by calling the [**ICertView::SetRestriction**](/windows/desktop/api/Certview/nf-certview-icertview-setrestriction) function. Qualifying criteria consists of informing the view to retrieve data based on qualifiers such as Greater Than, Less Than, Equal To, and so on.
4.  Call [**ICertView::OpenView**](/windows/desktop/api/Certview/nf-certview-icertview-openview) to retrieve the data in the view; the view's data will consist of the columns requested by means of [**ICertView::SetResultColumnCount**](/windows/desktop/api/Certview/nf-certview-icertview-setresultcolumncount) (and if a default view was not specified, [**ICertView::SetResultColumn**](/windows/desktop/api/Certview/nf-certview-icertview-setresultcolumn)). If [**ICertView::SetRestriction**](/windows/desktop/api/Certview/nf-certview-icertview-setrestriction) was called, data in the columns will be sorted and/or qualified. **ICertView::OpenView** creates a [**IEnumCERTVIEWROW**](/windows/desktop/api/Certview/nn-certview-ienumcertviewrow) object, which can be used to enumerate the view's rows.
5.  Use the [**IEnumCERTVIEWROW**](/windows/desktop/api/Certview/nn-certview-ienumcertviewrow) methods [**IEnumCERTVIEWROW::EnumCertViewAttribute**](/windows/desktop/api/Certview/nf-certview-ienumcertviewrow-enumcertviewattribute), [**IEnumCERTVIEWROW::EnumCertViewColumn**](/windows/desktop/api/Certview/nf-certview-ienumcertviewrow-enumcertviewcolumn), and [**IEnumCERTVIEWROW::EnumCertViewExtension**](/windows/desktop/api/Certview/nf-certview-ienumcertviewrow-enumcertviewextension) to retrieve attribute, column, and extension data as desired.

 

 

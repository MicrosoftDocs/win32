---
Description: 'The ICertView interface is used by properly authorized clients to view the Certificate Services database.'
ms.assetid: 'c8f316dd-186b-4e4a-b0ce-561a23b266cb'
title: Viewing the Certificate Services Database
---

# Viewing the Certificate Services Database

The [**ICertView**](icertview.md) interface is used by properly authorized clients to view the Certificate Services database. It should be noted that, as part of the shipped product, the Certification Authority MMC snap-in can be used to view the Certificate Services database. [**ICertView**](icertview.md) is provided for programmatically viewing the database. Support for the **ICertView** interface begins with Windows XP.

A properly authorized client means a user who has been granted permission to view the Certificate Services database; the Certification Authority MMC snap-in can be used to grant or restrict access to view the database (under **Properties** for the [*certification authority*](security.c_gly#-security-certification-authority-gly), click the **Security** tab). Additionally, to use the [**ICertView**](icertview.md) object, the client workstation is required to have installed the Certificate Services client components.

Although there are various scenarios for using [**ICertView**](icertview.md) and its related interfaces, the following depicts one possible sequence for developing a client application based on **ICertView**:

**To view the Certificate Services database**

1.  After obtaining an instance of the [**ICertView**](icertview.md) object, call [**ICertView::OpenConnection**](icertview2-openconnection.md) to communicate with a [*certification authority*](security.c_gly#-security-certification-authority-gly) on a specific computer.
2.  Call [**ICertView::SetResultColumnCount**](icertview2-setresultcolumncount.md) to specify the number of columns in the view; this call is also used to specify a default view. If a default view is not specified in the call, the caller must call [**ICertView::SetResultColumn**](icertview2-setresultcolumn.md) for each of the columns to be contained in the view.
3.  Optional. Specify sorting criteria and/or qualifying criteria for the database query by calling the [**ICertView::SetRestriction**](icertview2-setrestriction.md) function. Qualifying criteria consists of informing the view to retrieve data based on qualifiers such as Greater Than, Less Than, Equal To, and so on.
4.  Call [**ICertView::OpenView**](icertview2-openview.md) to retrieve the data in the view; the view's data will consist of the columns requested by means of [**ICertView::SetResultColumnCount**](icertview2-setresultcolumncount.md) (and if a default view was not specified, [**ICertView::SetResultColumn**](icertview2-setresultcolumn.md)). If [**ICertView::SetRestriction**](icertview2-setrestriction.md) was called, data in the columns will be sorted and/or qualified. **ICertView::OpenView** creates a [**IEnumCERTVIEWROW**](ienumcertviewrow.md) object, which can be used to enumerate the view's rows.
5.  Use the [**IEnumCERTVIEWROW**](ienumcertviewrow.md) methods [**IEnumCERTVIEWROW::EnumCertViewAttribute**](ienumcertviewrow-enumcertviewattribute.md), [**IEnumCERTVIEWROW::EnumCertViewColumn**](ienumcertviewrow-enumcertviewcolumn.md), and [**IEnumCERTVIEWROW::EnumCertViewExtension**](ienumcertviewrow-enumcertviewextension.md) to retrieve attribute, column, and extension data as desired.

 

 




---
title: How to Use built-in rights
description: This topic outlines the built-in rights that the Rights Management SDK 4.2 provides and usage restrictions that an app should enforce in honoring those restrictions.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '9142dd29-f1f4-4c2f-82ac-534f14b8bba1'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# How to: Use built-in rights

This topic outlines the built-in rights that the Rights Management SDK 4.2 provides and usage restrictions that an app should enforce in honoring those restrictions.

> [!Note]  
> For the Linux SDK, see the *rights.h* source file for details.

 

## Common Rights



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Right</strong><br/></td>
<td><strong>Values</strong><br/></td>
<td><strong>Description</strong><br/></td>
</tr>
<tr class="even">
<td>All<br/></td>
<td><ul>
<li>Android: [<strong>CommonRights.All</strong>](commonrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSCommonRights owner]</strong>](mscommonrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>CommonRights.All</strong>](commonrights-owner.md)</li>
<li>Linux: [CommonRights::All](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1CommonRights.mdl)</li>
</ul></td>
<td>A collection of all common rights.<br/></td>
</tr>
<tr class="odd">
<td>Owner<br/></td>
<td><ul>
<li>Android: [<strong>CommonRights.Owner</strong>](commonrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSCommonRights owner]</strong>](mscommonrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>CommonRights.Owner</strong>](commonrights-owner.md)</li>
<li>Linux: [CommonRights::Owner](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1CommonRights.mdl)</li>
</ul></td>
<td>The Owner right grants full control over the protected content.<br/></td>
</tr>
<tr class="even">
<td>View<br/></td>
<td><ul>
<li>Android: [<strong>CommonRights.View</strong>](commonrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSCommonRights view]</strong>](mscommonrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>CommonRights.View</strong>](commonrights-view.md)</li>
<li>Linux: [CommonRights::View](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1CommonRights.mdl)</li>
</ul></td>
<td>The right to view protected content. Typically, when this right is granted, the application enables the user to open and view protected content; however, additional rights are required to modify, extract, forward, or save the content.<br/></td>
</tr>
</tbody>
</table>



 

## Editable Document Rights



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Right</strong><br/></td>
<td><strong>Values</strong><br/></td>
<td><strong>Restrictions</strong><br/></td>
</tr>
<tr class="even">
<td>All<br/></td>
<td><ul>
<li>Android: [<strong>EditableDocumentRights.All</strong>](editabledocumentrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSEditableDocumentRights all]</strong>](mseditabledocumentrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>EditableDocumentRights.All</strong>](editabledocumentrights-all.md)</li>
<li>Linux: [EditableDocumentRights::All](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1EditableDocumentRights.mdl)</li>
</ul></td>
<td>A collection that contains all of the editable document rights. <br/></td>
</tr>
<tr class="odd">
<td>Comment<br/></td>
<td><ul>
<li>Android: [<strong>EditableDocumentRights.Comment</strong>](editabledocumentrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSEditableDocumentRights comment]</strong>](mseditabledocumentrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>EditableDocumentRights.Comment</strong>](editabledocumentrights--comment.md)</li>
<li>Linux: [EditableDocumentRights::Comment](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1EditableDocumentRights.mdl)</li>
</ul></td>
<td>The right to make comments on the document. <br/></td>
</tr>
<tr class="even">
<td>Edit<br/></td>
<td><ul>
<li>Android: [<strong>EditableDocumentRights.Edit</strong>](editabledocumentrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSEditableDocumentRights edit]</strong>](mseditabledocumentrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>EditableDocumentRights.Edit</strong>](editabledocumentrights-edit.md)</li>
<li>Linux: [EditableDocumentRights::Edit](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1EditableDocumentRights.mdl)</li>
</ul></td>
<td>The right to edit protected content and save it in the same protected format. Typically, when this right is granted, the app enables the user to change protected content and then save it to the same file.<br/></td>
</tr>
<tr class="odd">
<td>Export<br/></td>
<td><ul>
<li>Android: [<strong>EditableDocumentRights.Export</strong>](editabledocumentrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSEditableDocumentRights exportable]</strong>](mseditabledocumentrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>EditableDocumentRights.Export</strong>](editabledocumentrights-export.md)</li>
<li>Linux: [EditableDocumentRights::Export](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1EditableDocumentRights.mdl)</li>
</ul></td>
<td>The right to extract content from a protected format and place it in a different AD RMS-protected format. Typically, when this right is granted, the app enables the user to save protected content to other AD RMS-protected formats; for example, if the application implements a <em>Save As</em> functionality.<br/></td>
</tr>
<tr class="even">
<td>Extract<br/></td>
<td><ul>
<li>Android: [<strong>EditableDocumentRights.Extract</strong>](editabledocumentrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSEditableDocumentRights extract]</strong>](mseditabledocumentrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>EditableDocumentRights.Extract</strong>](editabledocumentrights-print.md)</li>
<li>Linux: [EditableDocumentRights::Extract](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1EditableDocumentRights.mdl)</li>
</ul></td>
<td>The right to extract content from a protected format and place it in an unprotected format. Typically, when this right is granted, the app enables the user to copy and paste information from protected content. If the app implements a <em>Save As</em> functionality, the application might also enable the user to save protected content to unprotected formats and other protected formats. This right has the same value as the Extract right for email.<br/></td>
</tr>
<tr class="odd">
<td>Print<br/></td>
<td><ul>
<li>Android: [<strong>EditableDocumentRights.Print</strong>](editabledocumentrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSEditableDocumentRights print]</strong>](mseditabledocumentrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>EditableDocumentRights.Print</strong>](editabledocumentrights-print.md)</li>
<li>Linux: [EditableDocumentRights::Print](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1EditableDocumentRights.mdl)</li>
</ul></td>
<td>The right to print protected content. Typically, when this right is granted, the app enables the user to print protected content. This right has the same value as the Print right for email.<br/></td>
</tr>
</tbody>
</table>



 

## Email Rights



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Right</strong><br/></td>
<td><strong>Values</strong><br/></td>
<td><strong>Restrictions</strong><br/></td>
</tr>
<tr class="even">
<td>All<br/></td>
<td><ul>
<li>Android: [<strong>EmailRights.All</strong>](emailrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSEmailRights all]</strong>](msemailrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>EmailRights.All</strong>](emailrights-all.md)</li>
<li>Linux: [EmailRights::All](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1EmailRights.mdl)</li>
</ul></td>
<td>A collection that contains all of the email rights.<br/></td>
</tr>
<tr class="odd">
<td>Extract<br/></td>
<td><ul>
<li>Android: [<strong>EmailRights.Extract</strong>](emailrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSEmailRights extract]</strong>](msemailrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>EmailRights.Extract</strong>](emailrights-extract.md)</li>
<li>Linux: [EmailRights::Extract](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1EmailRights.mdl)</li>
</ul></td>
<td>The right to extract content from a protected format and place it in an unprotected format. Typically, when this right is granted, the app enables an email recipient to copy and paste information from a protected message. If the app implements a <em>Save As</em> functionality, the application might also enable the recipient to save protected content to unprotected formats and other protected formats. This right has the same value as the Extract right for editable documents.<br/></td>
</tr>
<tr class="even">
<td>Forward<br/></td>
<td><ul>
<li>Android: [<strong>EmailRights.Forward</strong>](emailrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSEmailRights forward]</strong>](msemailrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>EmailRights.Forward</strong>](emailrights-forward.md)</li>
<li>Linux: [EmailRights::Forward](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1EmailRights.mdl)</li>
</ul></td>
<td>The right to forward a protected message. Typically, when this right is granted, the app enables an email recipient to forward a protected message.<br/></td>
</tr>
<tr class="odd">
<td>Print<br/></td>
<td><ul>
<li>Android: [<strong>EmailRights.Print</strong>](emailrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSEmailRights print]</strong>](msemailrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>EmailRights.Print</strong>](emailrights-print.md)</li>
<li>Linux: [EmailRights::Print](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1EmailRights.mdl)</li>
</ul></td>
<td>The right to print protected content. Typically, when this right is granted, the app enables an email recipient to print a protected message. This right has the same value as the Print right for editable documents.<br/></td>
</tr>
<tr class="even">
<td>Reply<br/></td>
<td><ul>
<li>Android: [<strong>EmailRights.Reply</strong>](emailrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSEmailRights reply]</strong>](msemailrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>EmailRights.Reply</strong>](emailrights-reply.md)</li>
<li>Linux: [EmailRights::Reply](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1EmailRights.mdl)</li>
</ul></td>
<td>Typically, when this right is granted, the app enables an email recipient to reply to a protected message and include a copy of the original message.<br/></td>
</tr>
<tr class="odd">
<td>ReplyAll<br/></td>
<td><ul>
<li>Android: [<strong>EmailRights.ReplyAll</strong>](emailrights-class-java.md)</li>
<li>iOS and OS X: [<strong>[MSEmailRights replyAll]</strong>](msemailrights-interface-objc.md)</li>
<li>Windows Store and Windows Phone: [<strong>EmailRights.ReplyAll</strong>](emailrights-replyall.md)</li>
<li>Linux: [EmailRights::ReplyAll](http://azuread.github.io/rms-sdk-for-cpp/classrmscore_1_1modernapi_1_1EmailRights.mdl)</li>
</ul></td>
<td>Typically, when this right is granted, the app enables an email recipient to reply to all recipients of a protected message and include a copy of the original message.<br/></td>
</tr>
</tbody>
</table>



 

 

 






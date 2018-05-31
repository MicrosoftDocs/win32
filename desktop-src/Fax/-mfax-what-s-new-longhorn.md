---
Description: This topic provides information on new Fax Service features for Windows Vista.
ms.assetid: 5a5a6f8c-3e1d-46eb-b2c5-d5449709deee
title: What's New in Windows Vista
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Windows Vista

This topic provides information on new Fax Service features for Windows Vista.

Several new interfaces enable developers to create and manage separate fax user accounts on the fax server. There are also a variety of enhanced security, configuration, and message management APIs.

## Fax Accounts

Windows Vista Fax is fully account-based. An accounts-based fax model enables small business users to configure, manage, and track their fax documents and resources easily and efficiently. It also enables the fax server to delegate the authentication of fax accounts to the standard Windows authentication module through which users are authenticated. A single user can have just one [fax account](-mfax-glossary.md) and one fax account can be used by just one user.

Advantages with the account-based model are listed below:

-   **Better privacy**. A user's faxes cannot be seen by another user.
-   **Better message organization**. The accounts concept is a well-understood paradigm in communications that enables better organization of messages. Fax users can manage their faxes in a way that is very similar to how they manage emails.
-   **Uniform access to fax servers**. Account-based organization gives users uniform access to different types of fax servers, such as Internet Fax Service Provider, Local Fax Modem, and Shared Fax Service.
-   **Reassignment**. Received faxes are sharable by default among fax users. Windows Vista Server enables a [routing administrator](-mfax-glossary.md) to assign inbox faxes to the correct users. (This is not supported in Windows Vista clients.) The administrator can delegate which users will be routing administrators. The administrator can also turn off the reassignment feature entirely.

## Sending Multiple Documents in a Single Fax

The Windows Vista Fax Service adds APIs that provide the ability to specify multiple documents in a single fax submission. Applications do not have a reliable way to print random documents or merge tiff files. With this support, fax-aware applications can specify multiple documents and the API generates tiff files for each document and merges them into one tiff file.

## Shell Extension for Fax

Improving the discoverability of fax features through Windows Explorer makes the Windows Vista Fax Service more accessible to the user. Now users can right-click a document in Explorer and select **Send to Fax Recipient**. Developers can also integrate the "Send to Fax Recipient" functionality into their applications by using the [**SendToFaxRecipient**](/previous-versions/windows/desktop/api/Fxsutility/nf-fxsutility-sendtofaxrecipient) API.

## New API for Windows Vista

The following new APIs are included in the Windows Vista release:

The existing [**FaxDocument**](-mfax-faxdocument.md), [**FaxOutgoingJob**](-mfax-faxoutgoingjob.md), [**FaxOutgoingMessage**](-mfax-faxoutgoingmessage.md) and [**FaxIncomingMessage**](-mfax-faxincomingmessage.md) objects provide default implementations of the new [**IFaxDocument2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdocument2), [**IFaxOutgoingJob2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingjob2), [**IFaxOutgoingMessage2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingmessage2) and [**IFaxIncomingMessage2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingmessage2) interfaces, respectively. There are no default implementations of the new [**IFaxServerNotify2**](/previous-versions/windows/desktop/api/FaxComex/) or [**IFaxAccountNotify**](/previous-versions/windows/desktop/api/FaxComex/) interfaces. All of the other new interfaces have a default implementation with a new object that has the same name as the interface, without the "I" at the beginning. For example, the default implementation of the new [**IFaxAccount**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccount) interface is the new [**FaxAccount**](-mfax-faxaccount.md) object.



| API Name                                                                  | Header       | Library        |
|---------------------------------------------------------------------------|--------------|----------------|
| [**CanSendToFaxRecipient**](/previous-versions/windows/desktop/api/Fxsutility/nf-fxsutility-cansendtofaxrecipient)              | fxsutility.h | fxsutility.dll |
| [**SendToFaxRecipient**](/previous-versions/windows/desktop/api/Fxsutility/nf-fxsutility-sendtofaxrecipient)                    | fxsutility.h | fxsutility.dll |
| [**IFaxAccount**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccount)                               | faxcomex.h   | fxscomex.dll   |
| [**IFaxAccountFolders**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountfolders)                 | faxcomex.h   | fxscomex.dll   |
| [**IFaxAccountIncomingArchive**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountincomingarchive) | faxcomex.h   | fxscomex.dll   |
| [**IFaxAccountIncomingQueue**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountincomingqueue)     | faxcomex.h   | fxscomex.dll   |
| [**IFaxAccountNotify**](/previous-versions/windows/desktop/api/FaxComex/)                      | faxcomex.h   | fxscomex.dll   |
| [**IFaxAccountOutgoingArchive**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountoutgoingarchive) | faxcomex.h   | fxscomex.dll   |
| [**IFaxAccountOutgoingQueue**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountoutgoingqueue)     | faxcomex.h   | fxscomex.dll   |
| [**IFaxAccounts**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccounts)                             | faxcomex.h   | fxscomex.dll   |
| [**IFaxAccountSet**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxaccountset)                         | faxcomex.h   | fxscomex.dll   |
| [**IFaxConfiguration**](/previous-versions/windows/desktop/api/Faxcomex/nn-faxcomex-ifaxconfiguration)                      | faxcomex.h   | fxscomex.dll   |
| [**IFaxDocument2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxdocument2)                           | faxcomex.h   | fxscomex.dll   |
| [**IFaxIncomingMessage2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxincomingmessage2)             | faxcomex.h   | fxscomex.dll   |
| [**IFaxOutgoingJob2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingjob2)                     | faxcomex.h   | fxscomex.dll   |
| [**IFaxOutgoingMessage2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxoutgoingmessage2)             | faxcomex.h   | fxscomex.dll   |
| [**IFaxSecurity2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxsecurity2)                           | faxcomex.h   | fxscomex.dll   |
| [**IFaxServer2**](/previous-versions/windows/desktop/api/FaxComex/nn-faxcomex-ifaxserver2)                               | faxcomex.h   | fxscomex.dll   |
| [**IFaxServerNotify2**](/previous-versions/windows/desktop/api/FaxComex/)                      | faxcomex.h   | fxscomex.dll   |



 

 

 




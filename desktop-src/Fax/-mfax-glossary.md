---
Description: This glossary defines some of the terms found in the documentation for the fax service.
ms.assetid: ede1c31f-e53a-4ddc-ba25-6fcadadd513a
title: Fax Service Glossary
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Fax Service Glossary

This glossary defines some of the terms found in the documentation for the fax service. Click a letter to jump to that section of the glossary, or use your browser's **Find** command to search for a word across the entire glossary.

[A](#a) [B](#b) [C](#c) [D](#d) E [F](#f) G H I [J](#j) K L [M](#m) N O P [Q](#q) [R](#r) S [T](#t) U V W X Y Z

## A

    **Archive**  The folder where successful faxes are stored. There is an outgoing archive (called Sent Items in the [Fax Console](#f)), where successfully sent faxes are stored, and an incoming archive (called Inbox in the Fax Console), where successfully received faxes are stored.

## B

    **Body**  The fax pages other than the cover page.

## C

    **Calling Subscriber ID**  The called station identifier (CSID) is a text string that identifies you as a fax recipient. It is transmitted to a fax sender, by the receiving device, when an incoming fax is detected. The CSID is often a combination of the fax number and business name. It is often the same as the transmitting station identifier (TSID).

    **CSID**  See [Calling Subscriber ID](#c).

## D

    **Document**  A fax that has not yet been submitted to a fax server. A document can consist of a cover page and body, but must include at least a cover page or body.

## F

    **Fax Account**  Fax Accounts enable small business users to configure, manage, and track their fax documents and resources very easily. It also enables the fax server to delegate the authentication of fax accounts to the standard Windows authentication module through which users are authenticated. One user can have one and only one fax account and one fax account can be used by one and only one user.

    **Fax body**  See [Body](#b).

    **Fax Console**  The fax service's user interface used to manage incoming and outgoing faxes.

    **Fax document**  See [Document](#d).

    **Fax job**  See [Job](#j).

    **Fax message**  See [Message](#m).

    **Fax Routing Extension**  A DLL used by the fax service, which exposes one or more inbound routing methods. These methods are used by the fax service to automatically route incoming faxes.

    **Fax Service Provider (FSP)**  A DLL used by the fax service that exposes one or more fax devices to the service. The DLL coordinates between the fax service and the fax device.

## J

    **Job**  An inbound or outbound fax transmission that is in a fax server's queue.

## M

    **Message**  A fax that a fax server has successfully received or transmitted and archived.

## Q

    **Queue**  The folder where faxes that are being processed (jobs) are stored. There is an outgoing queue (called Outbox in the [Fax Console](#f)), where faxes that are being sent are stored, and an incoming queue (called Incoming in the Fax Console), where faxes that are being received are stored.

## R

    **Routing Administrator**  The administrator can delegate some users as routing administrators. These routing administrators can assign the shared inbox faxes to the correct users.

    **Routing Assistant**   See [Routing Administrator](#r)

    **Reassign**  Assign the faxes in the inbox to the correct users. This action is performed by routing administrators.

## T

    **Tagged Image File Format**  See [TIFF](#t).

    **TIFF**  Tagged Image File Format (TIFF). A high-resolution, tag-based image format. TIFF is used for the universal interchange of digital images.

    **Transmitting Station ID**  TSID is a string that specifies the Transmitter Subscriber ID sent by the fax machine when sending a fax to a receiving machine. This string is usually a combination of the fax or telephone number and the name of the business. It is often the same as the [Calling Subscriber ID](#c).

    **TSID**  See [Transmitting Station ID](#t).

 

 




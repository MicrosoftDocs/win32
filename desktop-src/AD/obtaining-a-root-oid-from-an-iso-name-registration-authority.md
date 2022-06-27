---
title: Obtaining a Root OID from an ISO Name Registration Authority
description: The preferred way to obtain a root object identifier (OID) is to request one from an International Standards Organization (ISO) Name Registration Authority.
ms.assetid: ced5f475-bcfc-4546-9ec4-089e92414a4e
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining a Root OID from an ISO Name Registration Authority

The preferred way to obtain a root object identifier (OID) is to request one from an International Standards Organization (ISO) Name Registration Authority. This is a one-time action; when you have obtained a root OID, the OID space it defines is yours and you can administer it yourself.

There is usually a fee associated with registering an organization name and receiving a root OID. Fees and registration policies vary by country/region. In the United States, the ISO NRA is the American National Standards Institute (ANSI). For more information about the ANSI registration procedure and fee schedule, see https://ansi.org. The ISO maintains a list of member organizations at https://www.iso.org. If you are outside the United States, you should contact the ISO member organization for your country/region for name registration information.

Microsoft offers a script to generate a unique OID, which is not registered with a registration authority. This approach is sufficient for schema extensions you use in your own forests, where no external parties inquires about the OID registration. For more details on how to create such a base OID, see [Obtaining an Object Identifier from Microsoft](obtaining-an-object-identifier-from-microsoft.md).

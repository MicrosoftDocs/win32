---
description: Certificates are granted according to policies that define criteria that requesters must meet to receive a certificate.
ms.assetid: ad79dc0d-6457-4459-80e6-ab340436ecac
title: Policy Independence
ms.topic: article
ms.date: 05/31/2018
---

# Policy Independence

Certificates are granted according to policies that define criteria that requesters must meet to receive a certificate. For example, one policy may be to grant commercial certificates only if applicants present their identification in person. Another policy may grant [*credentials*](../secgloss/c-gly.md) based on email requests. An agency that issues credit cards may choose to consult a database and make phone inquiries before issuing a card.

Policies are implemented in policy modules written in C++, C, or Visual Basic. Certificate Services functions are isolated from any changes in policy that an agency might implement. Changes in policy can be fully implemented in the server policy module code. An enterprise [*certification authority*](../secgloss/c-gly.md) (CA) should use only the Microsoft-provided enterprise policy module.

 

 

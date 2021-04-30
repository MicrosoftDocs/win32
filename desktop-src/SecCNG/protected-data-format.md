---
description: Protected data is stored as an ASN.1 encoded BLOB.
ms.assetid: 8E287A1F-4EDF-4068-85F7-59A1D73F7BCD
title: Protected Data Format
ms.topic: article
ms.date: 05/31/2018
---

# Protected Data Format

Protected data is stored as an ASN.1 encoded BLOB. The data is formatted as CMS (certificate message syntax) enveloped content. The digital envelope contains encrypted content, recipient information that contains an encrypted content encryption key (CEK), and a header that contains information about the content, including the unencrypted protection descriptor rule string. This is shown by the following diagram.

![protected enveloped data](images/protecteddatablob.png)

## Related topics

<dl> <dt>

[CNG DPAPI](cng-dpapi.md)
</dt> <dt>

[Protection Descriptors](protection-descriptors.md)
</dt> <dt>

[Protection Providers](protection-providers.md)
</dt> </dl>

 

 




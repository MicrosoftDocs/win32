---
title: Obtaining a Link ID
description: Starting with Windows Server 2003, it is no longer necessary to request a linkID from Microsoft; there is a process for automatically generating a linkID.
ms.assetid: e3bf2936-40b1-46b5-8ee9-ab208bb388f6
ms.tgt_platform: multiple
keywords:
- Obtaining a Link ID
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining a Link ID

Starting with Windows Server 2003, it is no longer necessary to request a [**linkID**](/windows/desktop/ADSchema/a-linkid) from Microsoft; there is a process for automatically generating a **linkID**. The system will automatically generate a link ID for a new linked attribute when the attribute's **linkID** attribute is set to 1.2.840.113556.1.2.50. A back link for this forward link is created by setting the **linkID** to the [**attributeID**](/windows/desktop/ADSchema/a-attributeid) or [**ldapDisplayName**](/windows/desktop/ADSchema/a-ldapdisplayname) of the forward link. The schema cache must be reloaded after creating the forward link and before creating the back link. Otherwise, the forward link's **attributeId** or **ldapDisplayName** will not be found when the back link is created. The schema cache is reloaded on demand, a few minutes after a schema change is made, or when the DC is restarted. Create all forward links, reload the schema cache and then create all back links.

For example, when you have created the new attributes **myForwardLinkAttr** and **myBackLinkAttr**, and wish to link them:

> [!Note]  
> The OIDs in this example are contrived. See [Obtaining an Object Identifier from Microsoft](obtaining-an-object-identifier-from-microsoft.md) for instructions on obtaining OIDs for new attributes.

 

1.  Set these attributes on the attribute that is to be the forward link:
    ```C++
    ldapDisplayName: myForwardLinkAttr
    OID: 1.2.840.113556.6.1234
    LinkID: 1.2.840.113556.1.2.50
    ```

    

2.  Reload the Schema.
3.  Set these attributes on the attribute that is to be the back link:
    ```C++
    ldapDisplayName: myBackLinkAttr
    OID: 1.2.840.113556.6.1235
    LinkID: 1.2.840.113556.6.1234 or myForwardLinkAttr
    ```

    

## Related topics

<dl> <dt>

[Linked Attributes](linked-attributes.md)
</dt> <dt>

[How to Extend the Schema](how-to-extend-the-schema.md)
</dt> </dl>

 

 
---
description: You cannot create instances of the amended classes in the localized namespace. Amended classes in the localized namespace are treated as if they are abstract although they do not contain the Abstract qualifier.
ms.assetid: a0583153-f5d2-4f4c-ab2e-6ec468e665c7
ms.tgt_platform: multiple
title: Amended Class Considerations
ms.topic: article
ms.date: 05/31/2018
---

# Amended Class Considerations

You cannot create instances of the amended classes in the localized namespace. Amended classes in the localized namespace are treated as if they are abstract although they do not contain the [**Abstract**](standard-qualifiers.md) qualifier.

If you retrieve an amended class from a localized namespace using the WBEM\_FLAG\_USE\_AMENDED\_QUALIFIERS flag and spawn an instance from it, the instance contains all of the amended qualifiers of the amended class. You cannot store this new class in the namespace that contains the basic class definition unless you perform the **put** operation with the WBEM\_FLAG\_USE\_AMENDED\_QUALIFIERS flag. This flag instructs WMI to strip away any amended qualifiers before saving the object. If you do not specify WBEM\_FLAG\_USE\_AMENDED\_QUALIFIERS, the **put** operation fails with a WBEM\_E\_AMENDED\_OBJECT error.

 

 




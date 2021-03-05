---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 'e81068db-ab8e-420c-a0be-93bc92f3df6f'
title: Option Definitions
ms.topic: article
ms.date: 05/31/2018
---

# Option Definitions

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

The key consideration when you define an Option is to do so in such a way that it can be meaningfully compared to other Option instances contained in the same Feature. The comparison must be meaningful because the Option instance is used to define the configuration not just of the device, but of the job, independent of the device or PrintCapabilities that were used to create the configuration. The other Option instances in the Feature can appear either in the same PrintCapabilities document, or in another PrintCapabilities document that represents a different device, a PrintCapabilities document that is defined by another party working independently. After a client selects the device configuration to be used to render a job or document, that configuration typically is saved, along with the job or document, in the form of a PrintTicket. The PrintTicket contains a set of Option instances, typically one for each Feature defined in the PrintCapabilities document. Option instances must be portable and must preserve printing intent, so that the intent can be communicated when this PrintTicket is given to a different device, even one that has a different PrintCapabilities document that was written by a different author. The primary benefit of this portability is that if a different device does not specifically support an Option contained in the PrintTicket, the device driver or subsystem is able to identify and select the Option that is the closest in functionality.

One of the driver's main PrintTicket functions is to identify the device Option in the PrintCapabilities document that most closely matches a particular Option listed in the PrintTicket. During this matching or device driver defined scoring process, the Option in the PrintTicket is referred to as the *reference* Option, while the Option in the PrintCapabilities document is referred to as the *candidate* Option. The general matching metric is the number of matching ScoredProperty instances in the candidate and reference Option instances; a greater number of matches usually indicates better preservation of printing intent. In your scoring process you might choose to give greater weight to some ScoredProperty elements than to others.

You can make Option instances portable by ensuring that all Option instances that belong to the same Feature have one or more ScoredProperty *elements in common*. This means that there is a set of ScoredProperty elements that appears in every Option instance (belonging to the same Feature). For example, Option instances for the PageMediaSize Feature can be portable if every Option instance contains ScoredProperty elements that define the intrinsic PageMediaSize properties: MediaSizeWidth and MediaSizeHeight. The device driver or subsystem code can then determine how closely two Option instances agree by comparing the differences in these ScoredProperty values. If there is no Option in the PrintCapabilities document that exactly matches the one in the PrintTicket, the device driver can easily determine and select the Option that has the closest matching media dimensions.

Two objects (Option instances in this case) are said to have *elements in common*, or equivalently, have *corresponding elements*, if the following three conditions are satisfied.

1.  The two elements are of the same element type.

2.  The name attributes of the two elements are identical (or neither element contains a name attribute).

3.  The chain of parents of the elements being compared, up through the two objects under consideration, must satisfy conditions 1 and 2.

For example, consider a situation in which there are two Option instances, where each contains a ScoredProperty instance, and that each of these ScoredProperty instances contains a Property instance. Clearly, the first condition is satisfied (the two Property instances are the same type), and part of the third condition is satisfied (the parents of the Property instances are the same type, ScoredProperty, and the parents of those elements are the Option instances, which are also of the same type). If the name attributes of, respectively, the Property instances, the ScoredProperty instances, and the Option instances are either identical or are not supplied, the two Option instances have elements in common.

From the foregoing, the first step in creating Option instances is to define a set of ScoredProperty elements that are present in most or all of the Option instances. If your device configuration attribute can be represented by a standard Feature (one listed in the Print Schema Keywords), note the ScoredProperty elements in common in the standard Option instances. You should ensure that any new Option instances that you introduce also contain these ScoredProperty elements. You are always free to add additional ScoredProperty elements as needed to differentiate your Option instances from the standard Option instances. You may even delete one or more of the ScoredProperty elements in common if there is good reason, although that reduces the portability of such an Option. Of course, portability considerations suggest using the unmodified standard Option instances unless there is some intrinsic difference between your Option and the standard Option instance that must be reflected in the new Option instance.

The following example illustrates a situation for which you might wish to add a ScoredProperty element to an Option instance. All of the standard Option instances for the PageMediaSize Feature have the MediaSizeWidth and MediaSizeHeight ScoredProperty elements in common. Suppose that your device can support one of the standard Letter media sizes by feeding the paper either transversely (LongEdgeFirst) or longitudinally (ShortEdgeFirst). Assuming that you do not wish to introduce a new feed direction Feature to expose this degree of freedom, you can instead modify the two PageMediaSize Option instances for Letter to incorporate the paper feed orientation. For these two Letter Option instances, start with the standard PageMediaSize Option instance and add a new ScoredProperty element to represent the FeedDirection. In one Option instance, set the FeedDirection ScoredProperty to LongEdgeFirst; in the other Option instance, set FeedDirection to ShortEdgeFirst. Notice that these new Option instances maintain their portability. If the Option representing Letter, ShortEdgeFirst is saved to a PrintTicket and a different device that supports only the Letter standard Option is selected to render the Job, the Option-matching code can quickly determine that the standard Option Letter is the best match to the Option Letter, ShortEdgeFirst. The reason that this is the best match is that all of the ScoredProperty instances agree, with the exception of the FeedDirection ScoredProperty, which does not exist in the Letter standard Option.

You might also encounter cases where the modifications to the Option actually change the meaning so much that the modified Option can no longer be considered a specialized case of the original. In such cases, you should change the name of the Option to reflect the difference between the modified Option instance and the unmodified one. Only the author of the PrintCapabilities document for a particular device can decide whether the Option offered by the device differs sufficiently from a standard Option instance to warrant an incompatible definition.

Now consider the case where your device has a device configuration attribute that does not correspond to any of the standard Feature instances. In this case you cannot rely on the standard Option instances to provide the list of ScoredProperty elements in common. When you create a ScoredProperty instance, your main objective is to differentiate each Option from the others in the Feature, and describe why a user would select one Option over another. The baseline is to characterize each Option with a unique name attribute, and the ScoredProperty that holds the name attribute becomes the one used for determining elements in common.

After a set of ScoredProperty elements in common has been established, it is a simple matter to assign appropriate values to each ScoredProperty to create each Option. As in the previous example, for certain Option instances, you might need to add additional ScoredProperty instances or delete some of the elements in common to create an appropriate Option instance.

It should be noted that the Print Schema requires that the set of ScoredProperty instances, their locations, and the values assigned to each ScoredProperty in an Option must remain constant, independent of the configuration. The entire concept of the Print Schema relies on Option instances having fixed, identifiable Property and ScoredProperty instances that are shared across many devices.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




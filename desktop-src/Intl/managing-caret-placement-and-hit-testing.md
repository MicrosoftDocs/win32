---
description: Complex script languages are broken into clusters by ScriptShape. Character reordering always occurs within cluster boundaries. The clusters themselves are guaranteed to advance in the direction of the reading order.
ms.assetid: 50b4b643-af96-4a6f-80f9-27a71ce16b0e
title: Managing Caret Placement and Hit Testing
ms.topic: article
ms.date: 05/31/2018
---

# Managing Caret Placement and Hit Testing

Complex script languages are broken into [clusters](uniscribe-glossary.md) by [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape). Character reordering always occurs within cluster boundaries. The clusters themselves are guaranteed to advance in the direction of the reading order.

Cluster information in the logical cluster array is used to share the width of a cluster of glyphs equally among the logical characters they represent. For example, the lam alef glyph is divided into four areas:

-   The leading half of the lam.
-   The trailing half of the lam.
-   The leading half of the alef.
-   The trailing half of the alef.

Conventions for caret placement within clusters depend on the script. For the Arabic script, if the caret position is set between a base character and its combining mark, the caret is displayed halfway through the base character. For the Thai script, the caret cannot be positioned within a cluster. Thus, when the user advances the caret, the application must advance past all the glyphs that make up the cluster.

The [**ScriptXtoCP**](/windows/desktop/api/Usp10/nf-usp10-scriptxtocp) and [**ScriptCPtoX**](/windows/desktop/api/Usp10/nf-usp10-scriptcptox) functions translate between caret positions (in code point offsets) and x positions (in pixels). The **ScriptXtoCP** function has knowledge of the caret position conventions of each script:

-   For Indian and Thai, caret positions are snapped to cluster boundaries.
-   For Arabic, caret positions are interpolated with clusters.
-   For Hebrew, in versions prior to Usp10.dll, version 1.420, caret positions are interpolated with clusters. Beginning with Usp10.dll, version 1.420, caret positions are snapped to cluster boundaries.

Both [**ScriptXtoCP**](/windows/desktop/api/Usp10/nf-usp10-scriptxtocp) and [**ScriptCPtoX**](/windows/desktop/api/Usp10/nf-usp10-scriptcptox) operate only within runs. The functions require that certain parameters come from earlier Uniscribe calls, as shown in the following table.



| Parameter                                        | Source                                                 |
|--------------------------------------------------|--------------------------------------------------------|
| *psa*                                            | As returned by [**ScriptItemize**](/windows/desktop/api/Usp10/nf-usp10-scriptitemize). |
| *cGlyphspwLogClust*<br/> *psva*<br/> | As returned by [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape).     |
| *piAdvance*                                      | As returned by [**ScriptPlace**](/windows/desktop/api/Usp10/nf-usp10-scriptplace).     |



 

The application must establish the run in which a given caret offset or x position is before passing the information to [**ScriptCPtoX**](/windows/desktop/api/Usp10/nf-usp10-scriptcptox) or [**ScriptXtoCP**](/windows/desktop/api/Usp10/nf-usp10-scriptxtocp). If the application does not save the width information, it can do hit testing and caret placement after displaying each run. As an alternative, the application can cache enough information to do hit testing and caret placement on the current line without requiring reprocessing of the paragraph.

[**ScriptXtoCP**](/windows/desktop/api/Usp10/nf-usp10-scriptxtocp) returns a trailing edge value so that the application knows the side of the character or cluster on which the user has clicked. The value is either 0 or the width of the character or cluster in code points. The returned character position is the position of the character on which the user clicked. For more information, see [Displaying the Caret in Bidirectional Strings](displaying-the-caret-in-bidirectional-strings.md).

For languages such as Thai, for which the user conventionally does not want to place the caret into a cluster, [**ScriptXtoCP**](/windows/desktop/api/Usp10/nf-usp10-scriptxtocp) sets the trailing side flag to 0 or to the cluster width. For languages such as Arabic, for which the user expects to be able to edit within a cluster, **ScriptXtoCP** sets the trailing side flag to 0 or to 1.

To help the application establish valid locations for the caret when handling the arrow keys, Uniscribe provides information on valid caret positions in the **fCharStop** member in the logical attributes returned by [**ScriptBreak**](/windows/desktop/api/Usp10/nf-usp10-scriptbreak). **TRUE** is returned for most characters and **FALSE** for intercluster characters in scripts such as Thai. The application should check the **fNeedsCaretInfo** value in the [**SCRIPT\_PROPERTIES**](/windows/desktop/api/Usp10/ns-usp10-script_properties) structure for an item to see if it is necessary to call **ScriptBreak** to check for valid caret positions. If the **fNeedsCaretInfo** value is **FALSE**, all code points are valid caret positions.

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 





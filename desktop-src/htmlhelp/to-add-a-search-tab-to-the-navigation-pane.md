---
title: To add a Search tab to the Navigation pane
description: To add a Search tab to the Navigation pane
ms.assetid: 'A6AFABBB-3C10-415e-81DE-B85638412666'
---

# To add a Search tab to the Navigation pane

1.  [Enable full-text search](to-enable-full-text-search.md).
2.  Open a project (.hhp) file, and then click **Change Project Options**. 

    |                        |                                                                            |
    |------------------------|----------------------------------------------------------------------------|
    | ![](images/sb-cpo.gif) | Specifies files, compiler, window, and other project settings. <br/> |

    

     

3.  On the **Compiler** tab, select the **Compile full-text search information** check box, and then click **OK**.
4.  Click **Add/Modify Window Definitions**, and then click the **Navigation Pane** tab. 

    |                        |                                                                                                  |
    |------------------------|--------------------------------------------------------------------------------------------------|
    | ![](images/sb-adm.gif) | Adds or edits window definitions and the general appearance of the HTML Help Viewer. <br/> |

    

     

5.  In the **Window type** box, click the window you want, and then select the **Search tab** check box. Select the **Advanced** check box to add advanced full-text search features.

## Notes

-   You can decrease the time it takes for a full-text search by including a [full-text search stop list](to-add-a-full-text-search-stop-list-to-a-help-project.md) in your project. Any words in the stop list are omitted from the search. These are usually commonly occurring words, such as "the" or "and" that a user is unlikely to search for.
-   After you add a new tab, you may want to [adjust the window size and position](about-changing-the-size-and-position-of-a-window.md) of the Help Viewer to account for the new space the tab uses in the Navigation pane.

## Related topics

<dl> <dt>

[About Customizing the Help Viewer](customize-the-help-viewer.md)
</dt> </dl>

 

 






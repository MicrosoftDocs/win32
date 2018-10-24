---
Description: By setting the Factoid property to None, the character recognizer recognizes handwriting on a character-by-character basis.
ms.assetid: 4dacceab-032e-4b9b-858f-67961fd587b5
title: Word vs. Character Recognition
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Word vs. Character Recognition

By setting the [Factoid](https://msdn.microsoft.com/library/ms835848(v=MSDN.10).aspx) property to **None**, the character recognizer recognizes handwriting on a character-by-character basis.

The [RecoTimeout](https://msdn.microsoft.com/library/ms835852(v=MSDN.10).aspx) ([**RecoTimeout**](/windows/desktop/api/inked/nf-inked-iinkedit-get_recognitiontimeout) in Automation) property specifies the number of milliseconds of delay between the last [Stroke](https://msdn.microsoft.com/library/ms552692(v=VS.100).aspx) and the end of handwriting input. You can increase this value to recognize text before entire words or sentences are written. You can also force the recognition of ink immediately by using the [Recognize](https://msdn.microsoft.com/library/ms836275(v=MSDN.10).aspx) method.

 

 




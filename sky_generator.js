// The following block allows .indexOf to work for arrays
if (!Array.prototype.indexOf)
  Array.prototype.indexOf = (function(Object, max, min) {
    "use strict"
    return function indexOf(member, fromIndex) {
      if (this === null || this === undefined)
        throw TypeError("Array.prototype.indexOf called on null or undefined")

      var that = Object(this), Len = that.length >>> 0, i = min(fromIndex | 0, Len)
      if (i < 0) i = max(0, Len + i)
      else if (i >= Len) return -1

      if (member === void 0) {        // undefined
        for (; i !== Len; ++i) if (that[i] === void 0 && i in that) return i
      } else if (member !== member) { // NaN
        return -1 // Since NaN !== NaN, it will never be found. Fast-path it.
      } else                          // all else
        for (; i !== Len; ++i) if (that[i] === member) return i

      return -1 // if the value was not found, then return -1
    }
  })(Object, Math.max, Math.min)


var myDoc = app.activeDocument;
var skyLayer = myDoc.activeLayer;

//var fileName = File("C:/Users/kyles/OneDrive/Pictures/testing/test.jpg");
//var folderName = File("C:/Users/kyles/OneDrive/Pictures/testing/");
var idDatabaseArray = [];
//var idDatabase = File("C:/Users/kyles/OneDrive/Pictures/testing/00_unique_ids.txt");

if ( !(idDatabaseArray instanceof Array) )
  alert("idDatabaseArray is not an array");

for (var i = 1; i < 366; i++){
  //var fName = File(folderName + i + ".jpg");
  var fName = File("C:/Users/kyles/OneDrive/Pictures/lofi sky(dump)/" + i + ".jpg");
  generateNewImage(fName);
}

alert("Successfully generated new images!")

// ############################################################################
//  EOF
// ############################################################################

// Get random number between range
function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1) + min); //The maximum is inclusive and the minimum is inclusive
}

// Return image to original values
function resetImage(layer)
{
  executeAction( charIDToTypeID( "Rvrt" ), undefined, DialogModes.NO );
}

function generateNewImage(fileName)
{
  var shadowsArray = [getRandomIntInclusive(-100, 100), getRandomIntInclusive(-100, 100), getRandomIntInclusive(-100, 100)];
  var midsArray = [getRandomIntInclusive(-100, 100), getRandomIntInclusive(-100, 100), getRandomIntInclusive(-100, 100)];
  var highsArray = [getRandomIntInclusive(-100, 100), getRandomIntInclusive(-100, 100), getRandomIntInclusive(-100, 100)];

  var colorID; // store number sequence unique to each color
  colorID = shadowsArray.toString() + midsArray.toString() + highsArray.toString();
  colorID = colorID.replace(/[,-]/g,"");

  // check if color has already been used
  if ( idDatabaseArray.indexOf(colorID) > -1 )
  {
    generateNewImage(); // Calls function again until unique color is generated
  }
  else
  {
    idDatabaseArray.push(colorID); // put color ID in array
  }

  // check if the active layer is valid or error out otherwise
  if (skyLayer.typename === "ArtLayer")
  {
    // adjust brightness/contrast of image and assign unique color generated above
    skyLayer.adjustBrightnessContrast(getRandomIntInclusive(-50, 50), getRandomIntInclusive(-50, 50));
    skyLayer.adjustColorBalance(shadowsArray, midsArray, highsArray, true);

    // save the .psd document and export the image as .jpg
    myDoc.save;
    myDoc.exportDocument(fileName, ExportType.SAVEFORWEB);

    // do a 'revert' to go back original image values
    resetImage(skyLayer);

    fileName.close(); // close file
  }
  else
  {
    throw new Error('Program Terminated');
  }
}

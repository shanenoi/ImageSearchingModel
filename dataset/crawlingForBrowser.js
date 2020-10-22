/*  
 *  Paste these lines into ur browser's consolve, 
 *  And save base64, links content to each single file
 */

base64 = "";
links = "";

// class name is not stable, check it again before running this script
data = document.getElementsByClassName('bRMDJf islir')

for (i=0; i<data.length; i++) {
	temp = data[i].getElementsByTagName('img')[0].getAttribute('src') + "\n";
	if (temp.includes("jpeg;base64")) {
		base64 += temp.substr(23);
	} else if (temp.includes("http")) {
		links += temp;
	}
}

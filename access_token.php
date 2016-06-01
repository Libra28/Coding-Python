<?php

define('APP_ID', 'wx5c174c50435941e6');

define('APP_SECRET', '689bee27131ef4d87d520dd3319baafe');

function get_file_token() {
	if (exists_token()) {

		if (exprise_token()) {
			//重新获取一次，$token，并且将文件删除，重新向文件里面写一次
			$token = get_token();

			unlink('token.txt');
			file_put_contents('token.txt', $token);

		} else {

			$token = file_get_contents('token.txt');

		}

	} else {

		$token = get_token();

		file_put_contents('token.txt', $token);

	}
}

/*


完成获得到token 之后的业务逻辑代码


 */

//token.txt

//判断文件是否存在？
function exists_token() {

//判断token文件是否存在
	if (file_exists('token.txt')) {
		return true;
	} else {
		return false;
	}

}

//获取token.txt的创建时间，并且与当前执行index.php 文件的时间进行对比
function exprise_token() {
//文件创建时间
	$ctime = filectime('token.txt');

	if ((time() - $ctime) >= 7000) {
		return true;
	} else {
		return false;
	}
}

function get_token() {

	$ch = curl_init();

	$url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' . APP_ID . '&secret=' . APP_SECRET;

	curl_setopt($ch, CURLOPT_URL, $url);

	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

	curl_setopt($ch, CURLOPT_HEADER, 0);

	curl_setopt($ch, CURLOPT_TIMEOUT, 10);

	$output = curl_exec($ch);

	curl_close($ch);

	$obj = json_decode($output, true);

	//返回access_token
	return $obj['access_token'];

	var_dump($obj);
}

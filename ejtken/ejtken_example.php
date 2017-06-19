<?php
$x = [
    0.3,
    0.5,
    0.8,
    1
];

$y = [
    2.31,
    4.97,
    14.17,
    25.39
];


$P = [];
$point = 0.4;
$n = 4;

for ($i = 0; $i < 4; $i++) {
    $P[$i][$i] = $y[$i];
}
for ($j =0; $j < $n; $j++) {
    for ($i = $j - 1; $i >= 0; $i--) {

        echo "$i;$j===========\n";
        echo "1 / (x[$j]-x[$i])\n";
        $t = $j - 1;
        $k = $i + 1;
        echo "x - x[$i]; P[$i][{$t}]\n";
        echo "x - x[$j]; P[{$k}][$j]\n";
        $mult = 1 / ($x[$j] - $x[$i]);
        $P[$i][$j] = 1;
        echo "1 / ({$x[$j]} - {$x[$i]})\n";
        echo "{$point} - {$x[$i]};  {$P[$i][$j-1]}\n";
        echo "{$point} - {$x[$j]};  {$P[$i + 1][$j]}\n";
        $det = ((($point - $x[$i]) *  ($P[$i + 1][$j])) - ($P[$i][$j-1] * ($point - $x[$j])));
        echo "{$det} / " . ($x[$j] - $x[$i]) .  "\n";
        $P[$i][$j] = $mult * ((($point - $x[$i]) *  ($P[$i + 1][$j])) - ($P[$i][$j-1] * ($point - $x[$j])));
        echo "{$P[$i][$j]}\n";
    }
}

var_dump($P[0][$n - 1]);
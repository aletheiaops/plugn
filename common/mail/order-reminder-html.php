<?php

use yii\helpers\Html;

/* @var $this yii\web\View */
/* @var $order common\models\Order */
?>
<div class="verify-form">
    <h1>Dear <?= Html::encode($agent_name) ?>,</h1>

    <p class="lead">
      We would like to remind you that Order #<?= Html::encode($order->order_uuid) ?> has been placed 5 minutes ago for total amount of
        <?= \Yii::$app->formatter->asCurrency($order->total, $order->currency->code, [\NumberFormatter::MAX_SIGNIFICANT_DIGITS => $order->currency->decimal_place]) ?>
          <br/>
          <br/>
          <br/>
            Best Regards,
                <br/>
            Plugn Team
    </p>
</div>

% 生成示例数据
rng('default');
X = rand(100, 2);
y = (X(:, 1) + X(:, 2) > 1);

% 数据分割
cv = cvpartition(y, 'HoldOut', 0.3);
X_train = X(training(cv), :);
y_train = y(training(cv));
X_test = X(test(cv), :);
y_test = y(test(cv));

% 创建并训练 Logistic 回归模型
model = fitglm(X_train, y_train, 'Distribution', 'binomial', 'Link', 'logit');

% 进行预测
y_pred_prob = predict(model, X_test);
y_pred = round(y_pred_prob);

% 评估模型
accuracy = sum(y_pred == y_test) / length(y_test);
conf_matrix = confusionmat(y_test, y_pred);
class_report = classification_report(y_test, y_pred);

fprintf('Accuracy: %.2f\n', accuracy);
disp('Confusion Matrix:');
disp(conf_matrix);

% Helper function to generate classification report
function report = classification_report(y_true, y_pred)
    classes = unique(y_true);
    report = table;
    for i = 1:length(classes)
        class = classes(i);
        tp = sum((y_true == class) & (y_pred == class));
        fp = sum((y_true ~= class) & (y_pred == class));
        fn = sum((y_true == class) & (y_pred ~= class));
        precision = tp / (tp + fp);
        recall = tp / (tp + fn);
        f1 = 2 * (precision * recall) / (precision + recall);
        report = [report; table(class, precision, recall, f1)];
    end
    report.Properties.VariableNames = {'Class', 'Precision', 'Recall', 'F1_Score'};
end
